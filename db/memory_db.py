import uuid

from models.appointment import Appointment

# MemoryDB is a wrapper around the data stored in memory to emulate
# a database by exposing pre-set queries as methods
class MemoryDB:
    def __init__(self, doctors=[], appointments=[]):
        self.doctors = doctors
        self.appointments = appointments

    def get_all_doctors(self):
        return self.doctors

    def get_appointments(self, doctor_id=None, date=None, time=None):
        # assume input is valid
        appointments = self.appointments
        if doctor_id is not None:
            appointments = list(filter(lambda x: x['doctor_id'] == doctor_id, appointments))
        if date is not None:
            appointments = list(filter(lambda x: x['date'] == date, appointments))
        if time is not None:
            appointments = list(filter(lambda x: x['time'] == time, appointments))
        return appointments

    def create_appointment(self, doctor_id: str, new_appointment: Appointment):
        # assume input is valid
        appointment_id = str(uuid.uuid4()) # assume it is unique since it is uuid4
        new_appointment = {
            **new_appointment.dict(),
            'id': appointment_id,
            'doctor_id': doctor_id
        }
        self.appointments.append(new_appointment)
        return new_appointment

    def delete_appointment(self, appointment_id):
        # return the appointment that is deleted
        appointment = list(filter(lambda x: x['id'] == appointment_id, self.appointments))
        if len(appointment) == 0:
            return None
        
        self.appointments = list(filter(lambda x: x['id'] != appointment_id, self.appointments))
        return appointment
