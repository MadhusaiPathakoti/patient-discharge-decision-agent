import joblib
import os
import numpy as np
from app.models.ml.features import build_features


class ModelRegistry:
    def __init__(self):
        self.models = {}
        self._load_models()

    def _load_models(self):
        base_path = "app/models/ml/artifacts"

        model_paths = {
            "xgboost": f"{base_path}/xgboost.pkl",
            "logistic": f"{base_path}/logistic_regression.pkl",
        }

        for name, path in model_paths.items():
            if not os.path.exists(path):
                raise FileNotFoundError(f"Model file not found: {path}")

            self.models[name] = joblib.load(path)

        print(f"Loaded models: {list(self.models.keys())}")

    def predict_all(self, patient):
        features = np.array([build_features(patient)])
        predictions = {}

        for name, model in self.models.items():
            predictions[name] = float(model.predict_proba(features)[0][1])

        return predictions
