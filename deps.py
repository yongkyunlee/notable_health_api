# dependency injected to app
from data.initial_data import DOCTORS
from db.memory_db import MemoryDB


memoryDB = MemoryDB(doctors=DOCTORS)

def get_db() -> MemoryDB:
    return memoryDB
