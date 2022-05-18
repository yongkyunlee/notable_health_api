# dependency injected to app
from initial_data import DOCTORS
from memory_db import MemoryDB


memoryDB = MemoryDB(doctors=DOCTORS)

def get_db() -> MemoryDB:
    return memoryDB
