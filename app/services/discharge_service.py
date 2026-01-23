from app.models.ml.model_registry import ModelRegistry
from app.models.ml.model_selector import select_model
from app.decision_engine.rules import evaluate_rules
from app.decision_engine.composer import compose_decision
from app.decision_engine.explainer import generate_explanations


class DischargeService:
    def __init__(self):
        # Do NOT trigger model loading here
        self.registry = ModelRegistry()

    def make_decision(self, patient):
        model_preds = self.registry.predict_all(patient)
        selection = select_model(model_preds)

        risk_score = selection["risk_score"]
        rule_results = evaluate_rules(patient)

        decision_data = compose_decision(risk_score, rule_results)

        explanations = generate_explanations(
            risk_score,
            rule_results,
            decision_data["decision"],
            {"model_used": selection["model_used"]}
        )

        return {
            "patient_id": patient.patient_id,
            "decision": decision_data["decision"],
            "risk_score": risk_score,
            "model_used": selection["model_used"],
            "confidence": decision_data["confidence"],
            "explanations": explanations,
        }
