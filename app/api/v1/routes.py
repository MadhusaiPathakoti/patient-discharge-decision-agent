from fastapi import APIRouter
from app.models.schemas import PatientRequest, DecisionResponse
from app.services.discharge_service import DischargeService

router = APIRouter()
service = DischargeService()


@router.post("/decide-discharge", response_model=DecisionResponse)
def decide_discharge(request: PatientRequest):
    return service.make_decision(request)
