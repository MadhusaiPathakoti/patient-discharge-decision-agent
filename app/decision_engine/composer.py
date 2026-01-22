def compose_decision(risk_score: float, rule_results: dict) -> dict:
    """
    Combine ML risk score and rule outcomes to make final decision.
    """

    violated_critical_rules = [
        rule for rule, data in rule_results.items()
        if not data["passed"] and data["severity"] == "CRITICAL"
    ]

    violated_warning_rules = [
        rule for rule, data in rule_results.items()
        if not data["passed"] and data["severity"] == "WARNING"
    ]

    # 1️⃣ Safety-first escalation
    if violated_critical_rules:
        return {
            "decision": "ESCALATE_TO_DOCTOR",
            "confidence": 0.95
        }

    # 2️⃣ High risk → delay discharge
    if risk_score >= 0.7:
        return {
            "decision": "DELAY_DISCHARGE",
            "confidence": round(risk_score, 2)
        }

    # 3️⃣ Moderate risk + warnings
    if 0.4 <= risk_score < 0.7 and violated_warning_rules:
        return {
            "decision": "DELAY_DISCHARGE",
            "confidence": round(risk_score, 2)
        }

    # 4️⃣ Safe to discharge
    if risk_score < 0.4:
        return {
            "decision": "DISCHARGE",
            "confidence": round(1 - risk_score, 2)
        }

    # 5️⃣ Fallback safety net
    return {
        "decision": "ESCALATE_TO_DOCTOR",
        "confidence": 0.6
    }
