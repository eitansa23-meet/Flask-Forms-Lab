from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "eitan"
password = "123"
facebook_friends=["Daniel","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/' , methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if username == request.form['username'] and password == request.form['password']:
			return render_template('home.html')
		else:

			return render_template('login.html')
			
		
	else:
		return render_template('login.html')

@app.route('/home' , methods=['GET','POST'])
def go_home():
	return render_template('home.html')

			





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)