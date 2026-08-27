from fastapi import FastAPI

app = FastAPI()

@app.get("/text")
def get_text():
    return {"message": "Joaquin Vidal : APIs y programación - año"
    }