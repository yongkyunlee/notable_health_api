from pydantic import BaseModel

class Doctor(BaseModel):
    id: str
    first_name: str
    last_name: str
