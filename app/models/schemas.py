from pydantic import BaseModel
from typing import List

class PatientRequest(BaseModel):
    patient_id: str
    age: int
    heart_rate: int
    systolic_bp: int
    oxygen_level: int
    days_admitted: int
    previous_readmissions: int


class DecisionResponse(BaseModel):
    patient_id: str
    decision: str
    risk_score: float
    explanations: List[str]
