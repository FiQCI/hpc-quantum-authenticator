import requests
from flask import Blueprint, request, jsonify
from app.config import Config
from app.helpers import file_helper, validate_and_stringify
from app.logger import create_logger

logger = create_logger()
routes = Blueprint('routes', __name__)

@routes.get("/")
def welcome():
    return "<p>Welcome!</p>"

@routes.post('/token')
def create_token():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400

        required_keys = ['token', 'credential']
        request_values = validate_and_stringify(data, required_keys)
        if not request_values:
            return jsonify({'error': 'Missing authentication credential or token'}), 400

        if request_values['credential'] != Config.SECRET:
            return jsonify({'error': 'Invalid credentials'}), 401

        file_helper(request_values['token'], "create")
        return jsonify({'message': f'Token stored successfully'}), 201

    except Exception as e:
        logger.error('An error occurred: %s', str(e))
        return jsonify({'error': 'Something went wrong'}), 500


@routes.delete('/token')
def delete_token():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        required_keys = ['token', 'credential']
        request_values = validate_and_stringify(data, required_keys)

        if not request_values:
            return jsonify({'error': 'Missing authentication credential or token'}), 400
        
        if request_values['credential'] != Config.SECRET:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        file_helper(request_values['token'], "delete")
        return jsonify({'message': f'Token deleted successfully'}), 201
    
    except Exception as e:
        logger.error('An error occurred: %s', str(e))
        return jsonify({'error': 'Something went wrong'}), 500
    

@routes.post('/quantum/<token>/job')
def submit_job(token):
    try:
        token = str(token)
        quantum_data = request.get_json()
        
        if not quantum_data:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        if file_helper(token, "validate"):
            headers = {
                'Authorization': f'Bearer {Config.AUTH_TOKEN}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(Config.HELMI_URL, json=quantum_data, headers=headers)

            if response.status_code == 200:
                client_response = jsonify(response.json())
                client_response.status_code = response.status_code
                client_response.headers.pop('Content-Encoding', None)
                return client_response
            else:
                return jsonify({'error': 'Failed to submit job'}), response.status_code

        else:
            return jsonify({'error': 'Unauthorized'}), 401
    
    except Exception as e:
        logger.error('An error occurred: %s', str(e))
        return jsonify({'error': 'Something went wrong'}), 500