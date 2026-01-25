import random
import pandas as pd
import random

def generate_patient():
    age = random.randint(18, 90)
    heart_rate = random.randint(55, 120)
    systolic_bp = random.randint(80, 140)
    oxygen_level = random.randint(85, 100)
    days_admitted = random.randint(1, 10)
    previous_readmissions = random.randint(0, 4)

    # Risk scoring logic (hidden truth)
    risk_score = 0

    if oxygen_level < 92:
        risk_score += 3
    if systolic_bp < 90:
        risk_score += 3
    if heart_rate < 60 or heart_rate > 100:
        risk_score += 2
    if heart_rate > 110:
        risk_score += 2  # instead of +1
    if days_admitted < 2:
        risk_score += 2
    if previous_readmissions >= 2:
        risk_score += 3
    if age > 70:
        risk_score += 1

    prob = min(0.95, risk_score / 10)  # scale to probability
    readmitted = 1 if random.random() < prob else 0

    return {
        "age": age,
        "heart_rate": heart_rate,
        "systolic_bp": systolic_bp,
        "oxygen_level": oxygen_level,
        "days_admitted": days_admitted,
        "previous_readmissions": previous_readmissions,
        "readmitted": readmitted
    }


def generate_dataset(n=5000):
    data = [generate_patient() for _ in range(n)]
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_dataset()
    df.to_csv("data/synthetic/patient_readmission_data.csv", index=False)
    print("Synthetic dataset generated.")
