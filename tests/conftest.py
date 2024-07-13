import pytest
from kaspy.app import create_app

@pytest.fixture()
def app():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    flask_app.config.update({
        "TESTING": True,
    })

    # other setup can go here
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    # clean up / reset resources here
    ctx.pop()
    

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()