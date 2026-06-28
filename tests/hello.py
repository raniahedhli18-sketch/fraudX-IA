def test_hello(client):
    resp = client.get("/hello")

    assert resp.status_code == 200
    data = resp.get_json()

    assert data["message"] == "Welcome to FraudX AI"
