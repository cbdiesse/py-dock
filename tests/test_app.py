# import pytest
from tests.conftest import client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode()
    assert 'Hello, everyone ! ... hello Docker!' in html
