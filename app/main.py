from app.core.startup import ensure_models
from fastapi import FastAPI
from app.api.v1.routes import router
from app.core.logger import setup_logger

ensure_models()
setup_logger()

app = FastAPI(
    title="Patient Discharge Decision Agent",
    description="Decision Intelligence system for patient discharge",
    version="1.0.0"
)
@app.get("/")
def health_check():
    return {"status": "Patient Discharge Decision Agent is running"}

app.include_router(router, prefix="/api/v1")
