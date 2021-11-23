from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db" #name of database file #standard #tells app where to find db
app.config["SECRET_KEY"] = 'd65c5cbc4d268a8a431a06d5' #The secret key is needed to keep the client-side sessions secure.
#generate secret key in python shell: import os. os.urandom(12).hex() 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"     #tells login_required where the login page is located.
                                            #pass the name of login route in lowercase

login_manager.login_message_category = "info"   #login_required automatically displays a flash message .
                                                #setting the category message to info enables bootsrap to style
                                                #the flash message.

from market import routes


#A directory must contain a file named __init__.py in order for Python 
#to consider it as a package. This file can be left empty but we generally 
#place the initialization code for that package in this file.
 