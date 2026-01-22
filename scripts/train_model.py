import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, roc_auc_score


DATA_PATH = "data/synthetic/patient_readmission_data.csv"
MODEL_DIR = "app/models/ml/artifacts/"


def train_and_evaluate():
    df = pd.read_csv(DATA_PATH)

    X = df.drop("readmitted", axis=1)
    y = df["readmitted"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "random_forest": RandomForestClassifier(n_estimators=100),
        "xgboost": XGBClassifier(
            use_label_encoder=False,
            eval_metric="logloss"
        )
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        probs = model.predict_proba(X_test)[:, 1]

        results[name] = {
            "accuracy": accuracy_score(y_test, preds),
            "roc_auc": roc_auc_score(y_test, probs)
        }

        joblib.dump(model, f"{MODEL_DIR}{name}.pkl")

    print("Model Comparison:")
    for model, metrics in results.items():
        print(model, metrics)


if __name__ == "__main__":
    train_and_evaluate()
