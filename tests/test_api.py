from fraudx.app import create_app

app = create_app()

client = app.test_client()


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200


def test_hello():

    response = client.get(
        "/hello"
    )

    assert response.status_code == 200