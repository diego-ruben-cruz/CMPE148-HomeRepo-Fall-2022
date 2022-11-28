"""
    Description:	Python file for HW2. 
					Makes a flask server and sets up 
					multiple routes for different sub pages.
                    Builds on previous work by adding JWT authentication.

	Name: Diego Cruz
	SID: 013540384

	Course: CMPE 148
	Section: 02
	Homework: HW1
	Date: 16 October 2022 
"""
# imports the flask class
from flask import Flask

# Created an instance of a Flask and used __name__ as a shortcut
app = Flask(__name__)

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
