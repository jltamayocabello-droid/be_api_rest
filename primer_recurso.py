from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]

# Rutas dinamicas
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id,
            "name": "Guillermo Beltran"
            }

# Metodos
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

# Relaciones entre recursos

app.get("/users/{user_id}/orders")
def get_orders_for_user(user_id: int):
    return[
        {"order_id": 100, "user_id": user_id},
        {"order_id": 200, "user_id": user_id}
    ]

# Filtros, ordenamiento y paginación

@app.get("/users_pag")
def list_users(active: Optional[bool] = None, page: int=1, size: int=10):
    return{
        "active": active,
        "page": page,
        "size": size,
        "users":[]
    }