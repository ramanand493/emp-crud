import sys, os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hard to guess String'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/emp_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from crud.controllers import crud_controller
