import pytest
from kaspy import app

def test_index():
    client = app.create_app()
    response = client.get('/')
    assert response.status_code == 200