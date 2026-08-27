from fastapi import FastAPI
from datetime import datetime
from datetime import timezone

app = FastAPI()

# Endcoding UTF8
@app.get("/text")
def get_text():
    return {"message": "Joaquin Vidal : APIs y programación - año"
    }

# Manejo de fechas y horas en APIs

@app.get("/time")
def get_time():
    now = datetime.now(timezone.utc)
    iso_date = now.isoformat()

    return {"time": iso_date}
