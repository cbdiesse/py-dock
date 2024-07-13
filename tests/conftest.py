import pytest
from kaspy.app import create_app

@pytest.fixture(scope='session')
def test_client():
    test_app = create_app()
    test_app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield test_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()