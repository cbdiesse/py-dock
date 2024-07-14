import pytest
from kaspy.app import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True })
    with app.test_client() as client:
        yield client


@pytest.fixture()
def client2(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()