from pydantic import BaseModel
from typing import List, Optional


class PatientProfile(BaseModel):
    name: str
    age: int
    gender: str

    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None

    conditions: List[str] = []
    medications: List[str] = []
