from unittest.mock import patch

from fraudx.app import create_app

app = create_app()
client = app.test_client()


# ---------------------------
# HEALTH
# ---------------------------
def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200

    data = resp.get_json()
    assert data["status"] == "ok"
    assert "FraudX" in data["service"]


# ---------------------------
# HELLO
# ---------------------------
def test_hello():
    resp = client.get("/hello")
    assert resp.status_code == 200

    data = resp.get_json()
    assert data["message"] == "Welcome to FraudX AI"


# ---------------------------
# DB STATS (CSV REAL)
# ---------------------------
def test_db_stats():
    resp = client.get("/db/stats")

    assert resp.status_code == 200
    data = resp.get_json()

    assert data["transactions"] > 0
    assert data["frauds"] >= 0


# ---------------------------
# TRANSACTIONS (CSV REAL)
# ---------------------------
def test_transactions():
    resp = client.get("/db/transactions")

    assert resp.status_code == 200
    data = resp.get_json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]


# ---------------------------
# FRAUD PREDICT (MOCK OK ICI)
# ---------------------------


@patch("fraudx.app.predict_transaction")
def test_fraud_predict(mock_predict):
    mock_predict.return_value = {"fraud": 1, "score": 0.95}

    resp = client.post("/fraud/predict", json={"features": [1, 2, 3]})

    assert resp.status_code == 200
    data = resp.get_json()

    assert data["fraud"] == 1


def test_fraud_predict_missing():
    resp = client.post("/fraud/predict", json={})
    assert resp.status_code == 400


# ---------------------------
# FRAUD SUMMARY (CSV REAL)
# ---------------------------
def test_fraud_summary():
    resp = client.get("/fraud/summary")

    assert resp.status_code == 200
    data = resp.get_json()

    assert 0 <= data["fraud_rate"] <= 100
    assert data["total_transactions"] > 0
