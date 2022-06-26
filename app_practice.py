#import dependencies
from flask import Flask

#create a new Flask app instance
#app is name of new app instance, name is variable of current function
#you can use __name__ to see if code is being run from command line or has been imported into another piece of code
#variables with underscores before and after them are called magic methods in python
app = Flask(__name__)

#create first Flask app route
#define root (forward slash says we want to put data at the root of routes. The forward slash is commonly known as the highest level of hierarchy in any computer system)
@app.route("/")

#after making route, put code that you want in that specific route below the @app.route()
def hello_world():
    return "hello world"

#new route (practice)
@app.route("/")

def whats_going_on(text):
    print(text)

huh="What's going on?"

whats_going_on(huh)




# to run this file, navigate in terminal to the folder it's in, 
# activate the data environment
# type in export FLASK_APP=app.py
########This sets the FLASK_APP environment variable to the name of our Flask file, app.py
########Environment variables are dynamic variables on your computer and are used to modify the way a certain aspect of the computer operates
########For the FLASK_APP environment variable, we want to modify the path that will run our app.py so we can run the file 
# type in flask run
#It should say Running on: <your localhost address and port number> 
########A portnumber is the endpoint of a given program or service. Any Flask application you make can have whatever port number you want, most common is 5000
#copy and paste localhost address into web browser to see output