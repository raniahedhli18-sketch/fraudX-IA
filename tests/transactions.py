from unittest.mock import MagicMock, patch


@patch("fraudx.db.SessionLocal")
def test_transactions(mock_session, client):
    session = mock_session.return_value

    fake_row = MagicMock()
    fake_row.id = 1
    fake_row.amount = 100
    fake_row.fraud_label = 0

    session.query.return_value.limit.return_value.all.return_value = [fake_row]

    resp = client.get("/db/transactions")

    assert resp.status_code == 200

    data = resp.get_json()
    assert isinstance(data, list)
    assert data[0]["id"] == 1
    assert data[0]["amount"] == 100
