import enum

from pydantic import BaseModel


class AppointmentType(str, enum.Enum):
    new_patient = "New Patient"
    follow_up = "Follow-up"


class Appointment(BaseModel):
    patient_first_name: str
    patient_last_name: str
    appointment_type: AppointmentType
    date: str  # in yyyy-mm-dd format 
    time: str  # in HH-mm format
