from functools import lru_cache
from pathlib import Path

import joblib
import numpy as np

MODEL_PATH = Path("models/fraud_model.pkl")


@lru_cache(maxsize=1)
def get_model():
    return joblib.load(MODEL_PATH)


def predict_transaction(features):

    model = get_model()

    data = np.array(features).reshape(1, -1)

    probability = model.predict_proba(data)[0][1]

    prediction = "FRAUD" if probability >= 0.5 else "LEGIT"

    return {"prediction": prediction, "fraud_probability": round(float(probability), 4)}
