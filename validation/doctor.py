class DoctorExistsValidation:
    def __init__(self, doctors, doctor_id: str):
        self.doctors = doctors
        self.doctor_id = doctor_id

    def _validate_doctor_id_exists(self) -> None:
        for doctor in self.doctors:
            if doctor['id'] == self.doctor_id:
                return
        raise Exception(message=f"Doctor with id ${self.doctor_id} does not exist")

    def run(self) -> None:
        self._validate_doctor_id_exists()
