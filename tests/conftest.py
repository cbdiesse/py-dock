import pytest
from kaspy.app import create_app

@pytest.fixture(scope='session')
def test_client():
    test_app = create_app()
    testing_client = test_app.test_client()
    ctx = test_app.app_context()
    ctx.push()
    test_app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield test_client

    # clean up / reset resources here
    ctx.pop()
    

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()