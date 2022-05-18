import datetime

class DateFormatValidation:
    def __init__(self, date: str):
        self.date = date

    def _validate_date_format(self) -> None:
        # input date must have format 
        try:
            datetime.datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(message="Date must be in format 'YYYY-mm-dd'")

    def run(self) -> None:
        self._validate_date_format()

class TimeFormatValidation:
    def __init__(self, time: str):
        self.time = time

    def _validate_time_format(self) -> None:
        try:
            minute = datetime.datetime.strptime(self.time, "%H:%M").minute
        except ValueError:
            raise ValueError(message="Time must be in format 'HH:MM'")

        if minute not in [0, 15, 30, 45]:
            raise Exception(message="Minute must be in 15-minute intervals (0, 15, 30, 45)")
    
    def run(self) -> None:
        self._validate_time_format()

class DateTimeValidation:
    def __init__(self, date: str, time: str):
        self.date = date
        self.time = time
        self.date_format_validation = DateFormatValidation(date)
        self.time_format_validation = TimeFormatValidation(time)
    
    def _validate_datetime_in_future(self) -> None:
        # assume date and time formats have been validated
        date_time = datetime.datetime.strptime(f'{self.date} {self.time}', '%Y-%m-%d %H:%M')
        if date_time < datetime.datetime.now():
            raise Exception(message="Date time is in the past")

    def run(self) -> None:
        self.date_format_validation.run()
        self.time_format_validation.run()
        self._validate_datetime_in_future()
