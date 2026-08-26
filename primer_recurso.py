from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id,
            "name": "Guillermo Beltran"
            }

@app.post("/users")
def create_user():
    return {
        "message": "User created"
            }

# Versionado de APIs (URI y Header versioning)

@app.get("/api/v1/users")
def get_users_v1():
    return [
        {"id": 1, "name": "Guillermo Beltran"},
    ]

@app.get("/api/v2/users")
def get_users_v2():
    return [
        {"id": 1, "full_name": "Guillermo Beltran Rios"},
    ]