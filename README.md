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


# SOLID Principles in This Project

This project is designed using SOLID principles to ensure maintainability, extensibility, and production-readiness.
***Single Responsibility Principle (SRP)***
Each module has a single, well-defined responsibility:
API routing (routes.py)
Workflow orchestration (discharge_service.py)
ML prediction (model_registry.py)
Clinical rules (rules.py)
Decision composition (composer.py)
Explainability (explainer.py)

This separation makes the system easy to understand, test, and evolve.

***Open/Closed Principle (OCP)***
The system is open for extension but closed for modification:
New clinical rules can be added in rules.py without changing decision logic.
New ML models can be registered in model_registry.py without modifying orchestration or API layers.
This enables safe evolution of the platform.

***Liskov Substitution Principle (LSP)***
All ML models expose a consistent prediction interface (predict_proba), allowing models to be swapped or upgraded without impacting downstream decision logic.

***Interface Segregation Principle (ISP)***
The system avoids large, tightly coupled components. Each layer depends only on what it needs:
Rule engine is independent of ML internals.
ML layer is independent of clinical rules.
Explanation layer is independent of HTTP/API concerns.
This keeps interfaces small and focused.

***Dependency Inversion Principle (DIP)***
High-level workflow orchestration depends on abstractions (rule evaluation, model prediction, decision composition) rather than concrete implementations. This allows ML models, rules, and explanation strategies to be replaced or extended without changing core business flow.

***Summary***
By applying SOLID principles, the system achieves:
Clear separation of concerns
Safe extensibility for new models and rules
Improved testability and maintainability
Production-grade architecture suitable for regulated healthcare workflows

