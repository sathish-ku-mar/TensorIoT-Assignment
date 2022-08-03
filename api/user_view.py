import os, datetime
from flask import request, jsonify, Blueprint

from api.model import User
from core.validation import validateJson

users_api = Blueprint('users', __name__)


@users_api.route('/user/', methods=['GET'])
def home():
    responseObject = {
                "success": True,
                'message': 'Successfully lunched!...',
            }
    return jsonify(responseObject), 200


@users_api.route('/user/login/', methods=['POST'])
def login():
    """
    Validate the user credentials.
    """
    # Read ALL input  
    request_data = request.get_json()

    # Get the information    
    email = request_data.get("email", '')
    password = request_data.get("password", '')

    # Validate the input data
    validate = validateJson(request_data)
    if validate != None:
        return jsonify({"error":validate}), 400

    try:
        result = User.check_email_exist(email)
        if result:
            result.check_password(password)
    except Exception as err:
        return jsonify({"error":str(err)}), 400

    if result:
        result.last_login = datetime.datetime.utcnow()
        result.save()
        responseObject = {
            "success": True,
            'message': 'Successfully logged in.'
        }
        return jsonify(responseObject), 200
    else:
        return jsonify({'error':'Invalid credentials'}), 400


@users_api.route('/user/register/', methods=['POST'])
def register():
    """
    Store the user details in the User schema
    """
    # Read ALL input  
    request_data = request.get_json()

    # Get the information    
    name = request_data.get("name", '')
    email = request_data.get("email", '')
    password = request_data.get("password", '')

    # Validate the input data
    validate = validateJson(request_data)
    if validate != None:
        return jsonify({"error":validate}), 400

    # Check email already exist
    if User.check_email_exist(email):
        return jsonify({"error": "Email already exist"}), 400
    try:
        result = User(name,email,password)
        result.save()
    except Exception as err:
        return jsonify({"error":str(err)}), 400
    
    return {"success": True,
            "message": "User successfully created: "+ str(name)}, 200