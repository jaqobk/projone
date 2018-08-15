from flask import Flask, flash, redirect, render_template, request, session, abort, current_app, url_for
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from wtforms import Form, TextField, PasswordField, validators
import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
bootstrap = Bootstrap(app)
#Admin VIEW Here
admin = Admin(app, name='myapp', template_mode='bootstrap3')
#home template
@app.route('/')
def index():
	return render_template('home.html')
#end
#Start Login Template
@app.route('/login')
def login():
	return render_template('login.html')
#end Login template
@app.route('/contactus')
def contactus():
	return render_template('contactus.html')
#end contact template
#base 
@app.route('/base')
def base():
	return render_template('base.html')
#end base
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)