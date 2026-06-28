from unittest.mock import patch


@patch("fraudx.app.predict_transaction")
def test_fraud_predict_ok(mock_predict, client):
    mock_predict.return_value = {"fraud": 1, "score": 0.92}

    resp = client.post("/fraud/predict", json={"features": [1, 2, 3]})

    assert resp.status_code == 200
    assert resp.get_json()["fraud"] == 1


def test_fraud_predict_missing_json(client):
    resp = client.post("/fraud/predict")
    assert resp.status_code == 400


def test_fraud_predict_missing_features(client):
    resp = client.post("/fraud/predict", json={})
    assert resp.status_code == 400
