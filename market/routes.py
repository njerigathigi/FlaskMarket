from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)

@app.route("/register", methods=["GET", "POST"]) #allow route to handle web requests.(post and get)
 #get- send and the server returns data.
 #post- used to send html form data to the server.
def register_page():
    #generate secret key using import os, os.urandom(12).hex() in python shell.
    form = RegisterForm()
    if form.validate_on_submit(): #checks if user has clicked on the submit button of the form.
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for(market_page))#expects a hardcoded url but url_for helps us navigate this.

    return render_template('register.html', form=form)
