import joblib
import numpy as np
from app.models.ml.features import build_features


class ModelRegistry:

    def __init__(self):
        self.models = {
            "xgboost": joblib.load("app/models/ml/artifacts/xgboost.pkl"),
            "logistic": joblib.load("app/models/ml/artifacts/logistic_regression.pkl")
        }

    def predict_all(self, patient):
        features = np.array([build_features(patient)])
        predictions = {}

        for name, model in self.models.items():
            predictions[name] = float(model.predict_proba(features)[0][1])

        return predictions
