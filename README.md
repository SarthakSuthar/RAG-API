# Build a RAG API with FastAPI

**Project Link:** [View Project](http://nextwork.ai/projects/ai-devops-api)

**Author:** Sarthak Suthar  
**Email:** sarthaksuthar2804@gmail.com

---

---

## Introducing Today's Project!

In this project, I'm going to implement a RAG API. This will help me understand embading, vector db and AI response improvements. I'm interested in this because it helps me learn basics to become AI Engineer.

### Key tools and concepts

The key tools I used include Ollama, Python, and ChromaDB. Key concepts I learnt include embedding, chunking, ChormaDB operations.

### Challenges and wins

This project took me approximately 4 hrs.

---

## Performing RAG Manually

In this step, I'm going to demonstrate RAG directly in Ollama, then I will install required python dependencies. RAG stands for Retrival Augmented Generation.

![Image](http://nextwork.ai/secure_brown_proud_raspberry/uploads/ai-devops-api_v3j7x5b9)

### Understanding the three parts of RAG

I performed RAG manually by providing my data in prompt. The three parts are Retrival, Augmantation and Genera

### Comparing the two AI models

The key difference I noticed is nomic only generates embading numbers while qwen generates full on human readable response.

---

## Building a Personal Knowledge Base

In this step, I'm going to create my personal information file for retrieval and create python script for embaddings. Embeddings are converting text or data into numerical representation.

![Image](http://nextwork.ai/secure_brown_proud_raspberry/uploads/ai-devops-api_g3h7m2r5)

### Creating the profile document

I included information about my hobys and working profession. So when I ask about these detail, AI will look into this file and answer accordingly.

### How semantic search finds relevant chunks

When I ask a question, ChromaDB converts user's question into vector and matches with stored database vectors. It uses semantic search, instead of matching exact words, it matches by content with closest meaning.

---

## Creating the RAG API with FastAPI

In this step, I'm going to build an API that gives response to the /ask endpoint with my personal details. I'll test it using Swagger UI provided by FastAPI documentation.

![Image](http://nextwork.ai/secure_brown_proud_raspberry/uploads/ai-devops-api_j5m1r8t2)

### How the /ask endpoint works

When a question comes in, my endpoint first converts question into vector chunks. after converting to vector, it creates a content prompt for LLM and parses it to it for result generation. Then it returns a JSON with question, answer and Context used field.

### Testing with Swagger UI

I tested my API by asking what is my name and what I'm doing? The AI answered with JSON formate The context used was the first chunk.

---

## Extending to a Multi-User AI Directory

In this project extension, I'm adding multi-user support because every user has different details, so they can upload their data and use AI to answer their own personal questions. Multi-tenancy means an architecture where a single instance of a software application serves multiple customers, called "tenants." Each tenant shares the same application and database, but their data and configurations are isolated and remain invisible to other tenants.

![Image](http://nextwork.ai/secure_brown_proud_raspberry/uploads/ai-devops-api_d5g9k3n7)

### Adding the POST /documents endpoint

In this project extension, I added a POST endpoint that adds new data to ChromaDB. Metadata filtering allows finding data of a particular user by filtering it out using metadata.

![Image](http://nextwork.ai/secure_brown_proud_raspberry/uploads/ai-devops-api_r8t2w6y1)

### Verifying multi-user filtering

In this project extension, I tested multi-user queries by keeping the user field empty and filled on different requests to know if it really works. The filter works because on blank user, AI starts to hallucinate and gives answers from whole database, but if a user is provided, it responds only for that particular user
