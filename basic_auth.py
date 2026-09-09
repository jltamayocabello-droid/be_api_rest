from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic

app = FastAPI()

security = HTTPBasic()

@app.get("/secure-basic")
def secure_basic(credentials: str = Depends(security)):
    if credentials.username != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    if credentials.password != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    return {"message": "You are authenticated"}