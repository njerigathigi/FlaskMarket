from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)

@app.route("/register")
def register_page():
    #generate secret key using import os, os.urandom(12).hex() in python shell.
    form = RegisterForm()
    return render_template('register.html', form=form)
