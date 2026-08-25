from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]