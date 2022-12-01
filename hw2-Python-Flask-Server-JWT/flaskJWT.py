"""
    Description:	Python file for HW2. 
					
                    Makes a flask server and sets up 
					multiple routes for different sub pages.

                    Builds on previous work by adding JWT authentication
                    and database integration.

	Name: Diego Cruz
	SID: 013540384

	Course: CMPE 148
	Section: 02
	Homework: HW2
	Date: 30 November 2022
"""

# imports the used assets
from flask import Flask, request, jsonify, make_response, request, render_template, session, redirect
import jwt
from datetime import datetime, timedelta
from functools import wraps


# Created an instance of a Flask and used __name__ as a shortcut, template folder is set as a default dependency
app = Flask(__name__,template_folder='templates')
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
        # You can use the JWT errors in exception
        # except jwt.InvalidTokenError:
        #     return 'Invalid token. Please log in again.'
        except:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated


# Basic default route that offers a login page or a message communicating that you're logged in. 
@app.route('/')
def home():
    if session.get('logged_in') is None:
        return render_template('login.html')
    else:
        return 'logged in currently'

# Public route that can be access by all users, auth or not.
@app.route('/public')
def public():
    return 'For Public'

# auth only if you copy your token and paste it after /auth?query={insert_your_token_here}
# Hit enter and you will get the message below.
# Auth will give a message if your token is accepted.
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard !'

# Login page
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True

        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed!'})

# Logout page, resets session and redirects to default route
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)