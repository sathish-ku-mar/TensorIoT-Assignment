import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """
    User schema store the user rleated details
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    last_login = db.Column(db.DateTime)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def set_password(self, password):
        """
        Generate the hashed password
        :param password: Raw password
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Validate the user entered password
        :param password: Raw password
        """
        return check_password_hash(self.password_hash, password)

    def save(self):
        """
        Store the record in the DB and session
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_email_exist(cls, email):
        """
        Check the user entered email is exist or not
        :param email: User email id
        """
        return cls.query.filter_by(email=email).first()
