def test_fraud_summary(client):
    resp = client.get("/fraud/summary")

    assert resp.status_code == 200
    data = resp.get_json()

    assert 0 <= data["fraud_rate"] <= 100
