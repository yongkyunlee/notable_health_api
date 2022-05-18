# MemoryDB is a wrapper around the data stored in memory to emulate
# a database by exposing pre-set queries as methods
class MemoryDB:
    def __init__(self, doctors=[], appointments=[]):
        self.doctors = doctors
        self.appointments = appointments

    def get_all_doctors(self):
        return self.doctors

    def get_appointments(self, doctor_id=None, date=None):
        appointments = self.appointments
        if doctor_id is not None:
            appointments = list(filter(lambda x: x.doctor_id == doctor_id, appointments))
        if date is not None:
            appointments = list(filter(lambda x: x.date == date, appointments))
        return appointments

    def create_appointment(self, new_appointment):
        # assume input is valid
        pass

    def delete_appointment(self, appointment_id):
        # return the appointment that is deleted
        appointment = list(filter(lambda x: x.appointment_id == appointment_id, self.appointments))
        if len(appointment) == 0:
            return None
        
        self.appointments = list(filter(lambda x: x.appointment_id != appointment_id, self.appointments))
        return appointment
