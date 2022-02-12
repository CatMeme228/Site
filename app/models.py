from app import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default= datetime.utcnow())
    title= db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), nullable=False)
    userpassword = db.Column(db.Text(), nullable=False)