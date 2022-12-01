"""
    Description:	Python file for HW2. 
					
                    Makes a flask server and sets up 
					multiple routes for different sub-pages.

                    Builds on previous work by adding JWT authentication
                    and database access integration.

	Name: Diego Cruz
	SID: 013540384

	Course: CMPE 148
	Section: 02
	Homework: HW2
	Date: 30 November 2022
"""

# imports the used assets, mostly from flask but also a handful for use with the html file
from flask import Flask, request, jsonify, make_response, request, render_template, session, redirect
import jwt
from datetime import datetime, timedelta
from functools import wraps


# Creates an instance of a Flask and used __name__ as a shortcut,
# templates folder is set as a default dependency
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '83566d66ee8349d4b43d31d276207c6d'


def token_required(func):
    # decorator factory which invokes update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Message': 'Invalid token, please log in again'}), 403
        return func(*args, **kwargs)
    return decorated

# Basic default route
# If not authenticated, gives a form allowing you to enter your login info
# If already authenticated, gives a message informing you that you're already logged in


@app.route('/')
def home():
    if session.get('logged_in') is None:
        return render_template('login.html')
    else:
        return 'logged in currently'

# Public route that can be access by all users, authenticated or not
# Features basic message


@app.route('/public')
def public():
    return 'Public viewing page'

# Auth route
# Authenticates only if you copy your token and paste it after /auth?query={insert_your_token_here}
# Auth will give a message if your token is accepted
# If not authenticated, you will get a message saying your token is missing.
# Implementation does not work when logged in, jwt is valid when checked on jwt.io


@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard !'

# Login page
# Takes information from form and creates a jwt based on the information you entered
# Currently hard-coded to accept 'examplepassword' for sake of simplicity
# Can check token using jwt.io, use secret to encode


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == 'examplepassword':
        session['logged_in'] = True

        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed!'})

# Logout page
# Resets session and redirects to default route


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
