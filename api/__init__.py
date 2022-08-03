import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from api.user_view import users_api
from api.model import db

# Create App
app = Flask(__name__)

# load Config 
app.config.from_object('core.config.BaseConfig')

# Connect Flask and SqlAlchemy
db.init_app(app)

# Register the apps
app.register_blueprint(users_api)

Migrate(app,db)

# Enable CORS
CORS(app)

# Setup database
@app.before_first_request
def initialize_database():
    db.create_all()