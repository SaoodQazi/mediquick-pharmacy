import pytest
from app import create_app


@pytest.fixture
def app():
    """Create and configure a testing instance of the application."""
    test_app = create_app({"TESTING": True})
    return test_app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
