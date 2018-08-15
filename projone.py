from flask import Flask, render_template, Blueprint

from flask_bootstrap import Bootstrap
from flask_admin import Admin

app = Flask(__name__)
bootstrap = Bootstrap(app)
#Admin VIEW Here
admin = Admin(app, name='myapp', template_mode='bootstrap3')

#index template
@app.route('/')
def index():
    return render_template('home.html')

#home template
@app.route('/home')
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
@app.route('/base')
def base():
	return render_template('base.html')
#Start Footer
@app.route('/footer')
def footer():
	return render_template('footer.html')
#end footer


if __name__ == '__main__':
	app.run(debug=True)