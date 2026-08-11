import chromadb
import ollama
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)
from fastapi import APIRouter
from pydantic import BaseModel

client = chromadb.PersistentClient(path="./chroma_db")

ef = OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434",
)

collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef,
)


class DocumentSubmission(BaseModel):
    user_name: str
    content: str


que_router = APIRouter(prefix="/ask", tags=["ask"])
doc_router = APIRouter(prefix="/documents", tags=["documents"])


@que_router.get("/")
def ask(question: str, user: str | None = None):

    query_params = {
        "query_texts": [question],
        "n_results": 2,
    }

    if user:
        query_params["where"] = {"user_name": user}

    results = collection.query(**query_params)

    context = "\n\n".join(results["documents"][0])

    augmented_prompt = f"""Use the following context to answer the question.
If the context doesn't contain relevant information, say so.

Context:
{context}

Question: {question}"""

    response = ollama.chat(
        model="gemma3:1b", messages=[{"role": "user", "content": augmented_prompt}]
    )

    return {
        "question": question,
        "answer": response["message"]["content"],
        "context_used": results["documents"][0],
        "filtered_by_user": user,
    }


@doc_router.post("/")
def add_document(submission: DocumentSubmission):

    chunks = [
        chunk.strip() for chunk in submission.content.split("\n\n") if chunk.strip()
    ]

    collection.add(
        ids=[f"{submission.user_name}-chunk{i}" for i in range(len(chunks))],
        documents=chunks,
        metadatas=[
            {"source": "profile", "user_name": submission.user_name, "chunk_index": i}
            for i in range(len(chunks))
        ],
    )

    return {
        "message": f"Added {len(chunks)} chunks for user '{submission.user_name}'.",
        "user_name": submission.user_name,
        "chunks_added": len(chunks),
    }
