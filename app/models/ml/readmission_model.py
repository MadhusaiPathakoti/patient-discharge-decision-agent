import joblib
import shap
import numpy as np

from app.core.config import settings
from app.models.ml.features import build_features


FEATURE_NAMES = [
    "age",
    "heart_rate",
    "systolic_bp",
    "oxygen_level",
    "days_admitted",
    "previous_readmissions"
]


class ReadmissionModel:

    def __init__(self):
        self.model = joblib.load(settings.MODEL_PATH)
        self.explainer = shap.LinearExplainer(
            self.model,
            np.zeros((1, len(FEATURE_NAMES)))
        )

    def predict_risk(self, patient):
        features = np.array([build_features(patient)])
        return float(self.model.predict_proba(features)[0][1])

    def explain_prediction(self, patient):
        features = np.array([build_features(patient)])
        shap_values = self.explainer.shap_values(features)[0]

        explanation = {
            FEATURE_NAMES[i]: round(shap_values[i], 4)
            for i in range(len(FEATURE_NAMES))
        }

        return explanation
