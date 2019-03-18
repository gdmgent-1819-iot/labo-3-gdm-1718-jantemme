'''
Sensehat Dashboard
--------------------
Author: jantemme
Modified: 03-18-2019
--------------------
Installation:
sudo pip3 -U Flask
Docs: http://flask.pocoo.org/docs/1.0/
'''

# Import the libraries
from flask import Flask, jsonify, render_template, request
from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()
    
# Utilities
hex2rgb = lambda hx: (int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))

# Define the api_environment route
@app.route('/', methods=['GET', 'POST'])
def page():
    return "Data is being sent."

# Connect to firebase
cred = credentials.Certificate('./credential.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythonserver-8898f.firebaseio.com/'
})

ref = db.reference('/ambilight/')


def setLight():
    color = (hex2rgb(hex2rgb(ref.get()["color"])))
    sense.clear(color)

while(1):
    setLight()

# Main method for Flask server
if __name__ == '__main__':
  app.run(host = '192.168.5.198', port = 8081, debug = True)