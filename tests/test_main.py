from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_existing_item():
    response = client.post(
        "/stock/",
        json={
            "ticker": "QQQ",
            "start": "2022-07-22",
            "end": "2022-07-22"
        },
    )
    assert response.status_code == 200
