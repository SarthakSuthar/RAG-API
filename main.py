from fastapi import FastAPI

from router import doc_router, que_router

app = FastAPI()


app.include_router(doc_router)
app.include_router(que_router)


@app.get("/health")
def read_root():
    return {"status": "API working"}
