import os

class Settings:
    APP_ENV = os.getenv("APP_ENV", "dev")
    MODEL_PATH = os.getenv("MODEL_PATH", "app/models/ml/artifacts/model.pkl")

settings = Settings()
