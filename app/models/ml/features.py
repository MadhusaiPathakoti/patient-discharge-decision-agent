def build_features(patient):
    return [
        patient.age,
        patient.heart_rate,
        patient.systolic_bp,
        patient.oxygen_level,
        patient.days_admitted,
        patient.previous_readmissions,
    ]
