def test_db_stats(client):
    resp = client.get("/db/stats")

    assert resp.status_code == 200
    data = resp.get_json()

    assert data["transactions"] > 0
    assert data["frauds"] >= 0
