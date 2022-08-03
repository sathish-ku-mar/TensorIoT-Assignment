import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class BaseConfig():

    SQLALCHEMY_DATABASE_URI        = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get("SECRET_KEY", "TensorIOT")