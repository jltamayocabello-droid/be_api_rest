from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

VALID_TOKEN = "token_secreto_123"

@app.get("/secure-bearer")
def secure_bearer(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Header de autorización no enviado"
        )
        
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Formato Bearer incorrecto"
        )
        
    token = authorization.replace("Bearer ", "")
    
    if token != VALID_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Token no válido"
        )
        
    return {"message": "Token válido"}