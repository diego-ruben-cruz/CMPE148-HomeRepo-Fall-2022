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
from hmac import compare_digest

from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
# Created an instance of a Flask and used __name__ as a shortcut
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "flaskJWT_Python"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)

# route() tells flask what URL triggers our function
@app.route("/")
def homepage():
    return "<p>homepage</p>"
    # The function returns a basic "homepage" message.
    # You can make this more complicated by adding other routes for sub URLs.

@app.route("/hello-world")
def helloworld():
    return "<p>Hello, World!</p>"
    # The function returns a basic "Hello, World!" message.
    # You can make this more complicated by adding other routes for sub URLs.

@app.route("/hello-world/subURL-example")
def helloworldsub():
	return "<p>Hello, subURL!</p>"
	# The function returns a basic "Hello, subURL!" message.
