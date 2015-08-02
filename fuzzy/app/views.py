from flask import render_template, flash, redirect
from app import app
from mod_auth.forms import LoginForm
@app.route('/')
def hello():
    return 'Hello World'

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html',  title='Sign In', form=form)
