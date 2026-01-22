import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score


DATA_PATH = "data/synthetic/patient_readmission_data.csv"
MODEL_DIR = "app/models/ml/artifacts/"


def train_and_evaluate():
    os.makedirs(MODEL_DIR, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    X = df.drop("readmitted", axis=1)
    y = df["readmitted"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "xgboost": XGBClassifier(eval_metric="logloss"),
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        probs = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, probs)

        results[name] = auc
        joblib.dump(model, f"{MODEL_DIR}{name}.pkl")

    print("Model training complete. AUC scores:")
    for k, v in results.items():
        print(f"{k}: {v}")
