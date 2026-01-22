def select_model(predictions: dict) -> dict:
    """
    Select final risk score using confidence and agreement.
    """

    # Champion model
    champion_score = predictions["xgboost"]
    challenger_score = predictions["logistic"]

    # Agreement check
    if abs(champion_score - challenger_score) < 0.1:
        return {
            "risk_score": round(champion_score, 2),
            "model_used": "xgboost"
        }

    # Disagreement → safety escalation
    return {
        "risk_score": round(max(champion_score, challenger_score), 2),
        "model_used": "ensemble_safe_mode"
    }
