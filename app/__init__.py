from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C://Users//tolab//PycharmProjects//Site//database.db'

from app import views