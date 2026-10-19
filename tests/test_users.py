from app import create_app
from routes import users


def make_client():
    users.USERS.clear()
    return create_app().test_client()


BODY = {"name": "Ali", "email": "ali@example.com", "password": "secret123"}


def test_register_success():
    assert make_client().post("/register", json=BODY).status_code == 201


def test_duplicate_email_rejected():
    client = make_client()
    client.post("/register", json=BODY)
    assert client.post("/register", json=BODY).status_code == 409
