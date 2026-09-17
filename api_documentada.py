from fastapi import FastAPI, httpexception

app = FastAPI(
    title="API de usuarios",
    description="API para la gestión de usuarios con autenticación basica",
    version="1.0.0"
)

users = [
    {"id": 1, "name": "Miguel Beltran"},
    {"id": 2, "name": "Michael Rosales"}
    {"id": 3, "name": "Guillermo Beltran"}
]

@app.get("/users",
         summary="Obtener todos los usuarios",
         description="Obtiene una lista de todos los usuarios",
)

def get_users():
    return users

@app.get(
    "/users/{user_id}",
    summary="Obtener un usuario por ID",
    description="Devuelve los detalles de un usuario especifico dado su ID"   
 )

def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise httpexception.HTTPException(
        status_code=404, 
        detail="Usuario no encontrado"
        )

@app.post("/users",
         summary="Crear un nuevo usuario",
         description="Crea un nuevo usuario en la base de datos"
)

def create_user(user: dict):
    if "name" not in user:
        raise httpexception.HTTPException(
            status_code=400, 
            detail="El campo 'name' es obligatorio"
        )
    new_id = users[-1]["id"] + 1
    new_user = {"id": new_id, "name": user["name"]}
    users.append(new_user)
    return new_user