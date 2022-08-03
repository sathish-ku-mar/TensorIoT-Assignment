import os
from flask import request, jsonify, Blueprint

users_api = Blueprint('users', __name__)


@users_api.route('/user/', methods=['GET'])
def home():
    responseObject = {
                'status': 'success',
                'message': 'Successfully lunched!...',
            }
    return jsonify(responseObject), 200