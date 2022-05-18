from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from deps import get_db
from memory_db import MemoryDB
from models.appointment import Appointment
from models.doctor import Doctor

app = FastAPI()

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/doctors", response_model=List[Doctor])
async def get_all_doctors(db: MemoryDB = Depends(get_db)):
    return db.get_all_doctors()

@app.get("/doctors/{doctor_id}/appointments")
async def get_doctor_appointments(doctor_id: str):
    pass

@app.post("/doctors/{doctor_id}/appointments")
async def create_appointment(doctor_id: str, appointment: Appointment):
    pass

@app.delete("/appointments/{appointment_id}")
async def delete_appointment(appointment_id: str):
    pass
