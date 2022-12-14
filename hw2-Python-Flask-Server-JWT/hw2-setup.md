# How to set up and run a flask project with JWT

## Installation

    Install Python @ <https://https://www.python.org/downloads/>

    Create a virtual environment in cmdline or powershell by navigating to intended folder
    and using the following cmd or powershell input
    `py -3 -m venv venv`

    Activate the virtual environment by using the following cmd or powershell input
    `venv\Scripts\activate`

    Install the jwt command line interface using the following npm command in a separate powershell/cmd instance
    `npm install -g jwt-cli`

### If virtual environment activation fails, use the following powershell command

    `Set-ExecutionPolicy Unrestricted -Scope Process`

### After activating the virtual environment, use the following command to install flask and other assets.

    `pip install flask flask_jwt_extended flask_sqlalchemy PyJWT`

## To Run

    Inside of your virtual environment, use the basic commands:
    `flask --app flaskJWT run`
    OR
    `python -m flask --app flaskJWT run`

## Congrats! You have now successfully created and ran a flask project with JWT!
