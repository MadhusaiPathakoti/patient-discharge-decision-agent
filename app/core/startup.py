import os

from scripts.generate_synthetic_data import generate_dataset
from scripts.train_models import train_and_evaluate


def ensure_models():
    # Ensure data directory exists
    os.makedirs("data/synthetic", exist_ok=True)
    os.makedirs("app/models/ml/artifacts", exist_ok=True)

    # Step 1: Ensure synthetic data exists
    data_path = "data/synthetic/patient_readmission_data.csv"
    if not os.path.exists(data_path):
        print("Synthetic data not found. Generating...")
        df = generate_dataset()
        df.to_csv(data_path, index=False)
    else:
        print("Synthetic data found. Skipping generation.")

    # Step 2: Ensure models exist
    xgb_path = "app/models/ml/artifacts/xgboost.pkl"
    if not os.path.exists(xgb_path):
        print("Model artifacts not found. Training models...")
        train_and_evaluate()
    else:
        print("Model artifacts found. Skipping training.")
