from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "eitan"
password = "123"
facebook_friends=["Daniel","Nevo","Jude", "Issa", "Maya", "Ori"]


@app.route('/' , methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if username == request.form['username'] and password == request.form['password']:
			return redirect(url_for('go_home'))
		else:
			print("TRY AGAIN")
			return render_template('login.html')

			
		
	else:
		return render_template('login.html')

@app.route('/home' , methods=['GET','POST'])
def go_home():
	return render_template('home.html', facebook_friends = facebook_friends)

			
@app.route('/friend_exists/<string:name>' , methods=['GET','POST'])
def friend_exists(name):
	if name in facebook_friends:
		b = "True"
	else:
		b = "False"

	return render_template('friend_exists.html', n = name, b=b)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)