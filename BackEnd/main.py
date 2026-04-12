from fastapi import FastAPI

app = FastAPI()

@app.get("/api/message")
def read_message():
    return {"message": "Hello from FastAPI Backend!"}