# patient-discharge-decision-agent
# Decision Intelligence Philosophy

This system is designed as a Decision Intelligence platform, not a pure machine learning predictor.
Predictions are treated as inputs to decisions, which are further constrained by:
Clinical safety rules
Operational policies
Model governance logic
Explainability requirements
This ensures decisions are safe, transparent, and auditable.

# Safety-First Rule Hierarchy
Clinical rules are categorized by severity:
Severity	Meaning	Impact
CRITICAL	Patient safety risk	Immediate escalation
WARNING	Potential operational/clinical risk	May override ML
INFO	Contextual signal	Logged for audit
Example:
Oxygen < 92% → CRITICAL
Systolic BP < 90 → CRITICAL
Length of stay < 2 days → WARNING
This hierarchy ensures that no ML prediction can override critical clinical constraints.

# Multi-Model Governance (Champion–Challenger)

The system uses a champion–challenger architecture:
XGBoost → Champion (highest ROC-AUC)
Logistic Regression → Challenger (interpretability)
At runtime:
If models agree → trust champion
If models disagree → conservative fallback
This improves robustness and supports model risk management.

# Rule vs ML Conflict Resolution

The system explicitly supports cases where rules override ML predictions.
Example:
A patient with:
Low ML readmission risk
Very short length of stay (<2 days)
Even if ML predicts low risk, the system may:
Delay discharge
Escalate for review
This reflects real hospital policy where workflow safety can override statistical confidence.

# Explainability by Design

Every decision includes:
Rule-based explanations (clinical)
Model governance explanations (which model influenced decision)
This makes decisions suitable for:
Clinician trust
Auditing
Regulatory review

# Edge Case Handling
During testing, an edge case was identified where:
ML predicted low readmission risk
Patient had very short length of stay
The system was updated to treat short stay as a WARNING-level rule, enabling workflow policies to override ML in borderline cases.
This demonstrates continuous system improvement based on real-world testing.
