def generate_explanations(
    risk_score: float,
    rule_results: dict,
    decision: str,
    shap_explanation: dict
) -> list:
    explanations = []

    # Rule explanations
    for rule, data in rule_results.items():
        if not data["passed"]:
            explanations.append(
                f"{rule.replace('_', ' ').title()} violated "
                f"(value: {data['value']}, threshold: {data['threshold']})"
            )

    # SHAP-based ML explanations
    sorted_shap = sorted(
        shap_explanation.items(),
        key=lambda x: abs(x[1]),
        reverse=True
    )[:3]

    for feature, value in sorted_shap:
        if value > 0:
            explanations.append(
                f"{feature.replace('_', ' ').title()} increased readmission risk"
            )
        else:
            explanations.append(
                f"{feature.replace('_', ' ').title()} reduced readmission risk"
            )

    # Risk summary
    explanations.append(
        f"Predicted readmission risk score: {round(risk_score, 2)}"
    )

    # Decision reasoning
    if decision == "ESCALATE_TO_DOCTOR":
        explanations.append(
            "Decision escalated due to combined clinical and model risk"
        )

    return explanations
