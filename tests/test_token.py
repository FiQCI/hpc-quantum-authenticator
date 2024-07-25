import pytest
import secrets
from flask import Flask, jsonify, request
from app import create_app
from app.config import Config


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def random_token():
    return secrets.token_hex(16)

def test_create_token_invalid_json(client):
    response = client.post('/token', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid JSON'}

def test_create_token_missing_fields(client):
    response = client.post('/token', json={
        'token': 'test_token'
    })
    assert response.status_code == 400
    assert response.json == {'error': 'Missing authentication credential or token'}

def test_create_token_invalid_credentials(client):
    response = client.post('/token', json={
        'token': 'test_token',
        'credential': 'wrong_secret'
    })
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid credentials'}

def test_create_token_success(client, random_token):
    response = client.post('/token', json={
        'token': random_token,
        'credential': Config.SECRET
    })
    assert response.status_code == 201
    assert response.json == {'message': 'Token stored successfully'}

def test_create_token_when_file_exists(client, random_token):
    response = client.post('/token', json={
        'token': random_token,
        'credential': Config.SECRET
    })
    assert response.status_code == 201
    assert response.json == {'message': 'Token stored successfully'}



def test_delete_token_invalid_json(client):
    response = client.delete('/token', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid JSON'}

def test_delete_token_missing_fields(client):
    response = client.delete('/token', json={
        'credential': Config.SECRET
    })
    assert response.status_code == 400
    assert response.json == {'error': 'Missing authentication credential or token'}

def test_delete_token_invalid_credentials(client):
    response = client.delete('/token', json={
        'token': 'test_token',
        'credential': 'wrong_secret'
    })
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid credentials'}

def test_delete_token_success(client, random_token, monkeypatch):
    response = client.delete('/token', json={
        'token': random_token,
        'credential': Config.SECRET
    })
    assert response.status_code == 201
    assert response.json == {'message': 'Token deleted successfully'}

def test_delete_token_when_file_not_exists(client, random_token, monkeypatch):
    response = client.delete('/token', json={
        'token': "random_token",
        'credential': Config.SECRET
    })
    assert response.status_code == 201
    assert response.json == {'message': 'Token deleted successfully'}