"""
    Description: Python file for HW1. Used 

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
def hello_world():
    return "<p>Hello, World!</p>"
    # The function returns a basic "Hello, World!" message.
    # You can make this more complicated by adding other routes for sub URLs.
