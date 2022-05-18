from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from deps import get_db
from db.memory_db import MemoryDB
from models.appointment import Appointment
from models.doctor import Doctor
from validation.appointment import AppointmentExistsValidation, AppointmentInputValidation
from validation.date_time import DateFormatValidation, DateTimeValidation
from validation.doctor import DoctorExistsValidation

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


@app.get("/doctors/{doctor_id}/appointments/{date}", response_model=List[Appointment])
async def get_doctor_appointments(
    doctor_id: str,
    date: str,
    db: MemoryDB = Depends(get_db)
):
    doctor_id_validation = DoctorExistsValidation(db.get_all_doctors(), doctor_id)
    try:
        doctor_id_validation.run()
    except:
        raise HTTPException(status_code=404, detail=f"Doctor with id {doctor_id} not found")

    date_validation = DateFormatValidation(date)
    try:
        date_validation.run()
    except:
        raise HTTPException(status_code=422, detail=f"Wrong date format")

    appointments = db.get_appointments(doctor_id=doctor_id, date=date)
    print(f"Fetched {len(appointments)} appointments for doctor {doctor_id} on date {date} from db")

    return appointments


@app.post("/doctors/{doctor_id}/appointments")
async def create_appointment(
    doctor_id: str,
    appointment: Appointment,
    db: MemoryDB = Depends(get_db)
):
    # if we use a real database, we should use transaction
    doctor_id_validation = DoctorExistsValidation(db.get_all_doctors(), doctor_id)
    try:
        doctor_id_validation.run()
    except:
        raise HTTPException(status_code=404, detail=f"Doctor with id {doctor_id} not found")

    appointment_validation = AppointmentInputValidation(
        db.get_all_doctors(),
        db.get_appointments(doctor_id=doctor_id, date=appointment.date, time=appointment.time),
        appointment
    )
    try:
        appointment_validation.run()
    except:
        raise HTTPException(status_code=422, detail=f"Wrong input appointment")
    
    new_appointment = db.create_appointment(doctor_id, appointment)
    return new_appointment

@app.delete("/appointments/{appointment_id}")
async def delete_appointment(
    appointment_id: str,
    db: MemoryDB = Depends(get_db)
):
    appointment_id_validation = AppointmentExistsValidation(db.get_appointments(), appointment_id)
    try:
        appointment_id_validation.run()
    except:
        raise HTTPException(status_code=404, detail=f"Appointment with id {appointment_id} not found")

    deleted_appointment = db.delete_appointment(appointment_id)
    return deleted_appointment
