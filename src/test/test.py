import pytest
from flask import Flask
from flask_frozen import Freezer
from src.app import app  # Import the app from your src.app module

@pytest.fixture
def client():
    """Fixture to set up the Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route of the application."""
    response = client.get("/")  # Make a GET request to the index route
    assert response.status_code == 200  # Check if the response code is 200
    assert b"<html>" in response.data  # Check if the response contains <html>
