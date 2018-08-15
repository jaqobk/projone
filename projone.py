from flask import Flask, render_template, Blueprint

from flask_bootstrap import Bootstrap
from flask_admin import Admin

app = Flask(__name__)
bootstrap = Bootstrap(app)
#index template
@app.route('/')
def index():
    return '<h1>Here I am with my coding manenos</h1>'
@app.route('/home')
#home template
def home():
	return render_template('home.html')
#login template
@app.route('/login')
def login():
	return render_template('login.html')
#end login template
#start contact us templates
@app.route('/contactus')
def contactus():
	return render_template('contactus.html')
#end contact template
#test nav
@app.route('/nav')
def nav():
	return render_template('nav.html')


if __name__ == '__main__':
	app.run(debug=True)