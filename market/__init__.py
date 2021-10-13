from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
db = SQLAlchemy(app)

from market import routes

#A directory must contain a file named __init__.py in order for Python 
#to consider it as a package. This file can be left empty but we generally 
#place the initialization code for that package in this file.
