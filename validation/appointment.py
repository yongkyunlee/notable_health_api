
from models.appointment import Appointment
from validation.date_time import DateTimeValidation

class AppointmentExistsValidation:
    def __init__(self, appointments, appointment_id: str):
        self.appointments = appointments
        self.appointment_id = appointment_id
    
    def _validate_appointment_exists(self):
        for appointment in self.appointments:
            if appointment.id == self.appointment_id:
                return
        raise Exception(message=f"Appointment with id {self.appointment_id} does not exist")

class AppointmentInputValidation:
    def __init__(self, doctors, appointments, doctor_id: str, new_appointment: Appointment):
        self.doctors = doctors
        self.appointments = appointments
        self.doctor_id = doctor_id
        self.new_appointment = new_appointment
        self.datetime_validation = DateTimeValidation(new_appointment.date, new_appointment.time)

    def _validate_appointment_available(self) -> None:
        # validate that there are no more than 3 appointments
        if len(self.appointments) >= 3:
            raise Exception(message=f"No more than 3 appointments can be booked in a single time slot")

    def run(self) -> None:
        self.datetime_validation.run()
        self._validate_appointment_available()
