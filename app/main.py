from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import router
from app.core.startup import ensure_models
from app.core.logger import setup_logger

setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ===== STARTUP LOGIC =====
    ensure_models()
    yield
    # ===== SHUTDOWN LOGIC =====
    # (Nothing needed for now)


app = FastAPI(
    title="Patient Discharge Decision Agent",
    version="1.0.0",
    lifespan=lifespan
)

# ===== ADD ROOT HEALTH ENDPOINT HERE =====
@app.get("/")
def root():
    return {
        "service": "Patient Discharge Decision Agent",
        "status": "running",
        "docs": "/docs"
    }

# CORS for UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # demo only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(router, prefix="/api/v1")
