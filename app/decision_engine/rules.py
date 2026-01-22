from typing import Dict


CRITICAL_RULES = {
    "oxygen_level": "Oxygen saturation below safe threshold",
    "blood_pressure": "Low systolic blood pressure",
    "heart_rate": "Abnormal heart rate"
}


def evaluate_rules(patient) -> Dict:
    """
    Evaluate clinical and operational rules.
    Returns rule outcomes + severity.
    """

    results = {
        "oxygen_level": {
            "passed": patient.oxygen_level >= 92,
            "value": patient.oxygen_level,
            "threshold": 92,
            "severity": "CRITICAL"
        },
        "blood_pressure": {
            "passed": patient.systolic_bp >= 90,
            "value": patient.systolic_bp,
            "threshold": 90,
            "severity": "CRITICAL"
        },
        "heart_rate": {
            "passed": 60 <= patient.heart_rate <= 100,
            "value": patient.heart_rate,
            "threshold": "60-100",
            "severity": "WARNING"
        },
        "length_of_stay": {
            "passed": patient.days_admitted >= 2,
            "value": patient.days_admitted,
            "threshold": 2,
            "severity": "INFO"
        }
    }

    return results
