from src.ext import db
from src.models.BaseModel import BaseMod
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model, BaseMod, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False) 
    age = db.Column(db.Date, nullable=False)
    role = db.Column(db.String )
    gender = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_admin(self):
        return self.role == "admin"





