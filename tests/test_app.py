import pytest
# from kaspy import app

def test_index(client):
    # client = app.create_app()
    response = client.get('/')
    html = response.data.decode()
    assert 'Hello, everyone ! ... hello Docker!' in html
    assert response.status_code == 200
