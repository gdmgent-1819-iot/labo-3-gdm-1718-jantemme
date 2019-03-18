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
from pyrebase import pyrebase
import sys
import os

config = {
    "apiKey": "AIzaSyCtYneqq7WMa3-tLCZwlEhh4Mrn6GtHTpg",
    "authDomain": "pythonserver-8898f.firebaseapp.com",
    "databaseURL": "https://pythonserver-8898f.firebaseio.com",
    "projectId": "pythonserver-8898f",
    "storageBucket": "pythonserver-8898f.appspot.com",
    "messagingSenderId": "101060210218"
}
firebase = pyrebase.initialize_app(config)

try:
    #connect to firebase
    db = firebase.database()

    # Create an instance of flask
    app = Flask(__name__)

    # Create an instance of the sensehat
    sense = SenseHat()
        
    # Utilities
    hex2rgb = lambda hx: (int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))

    # Define the route
    @app.route('/', methods=['GET', 'POST'])
    def page():
        return "Data is being sent."

    def setLight():
        if (db.child('ambilight').get().val()):
            hexColor = db.child('ambilight').get().val()
            rgbColor = hex2rgb(hexColor)
            sense.clear(rgbColor)

    while(1):
        setLight()

    # Main method for Flask server
    if __name__ == '__main__':
        app.run(host = '192.168.5.198', port = 8081, debug = True)

except (KeyboardInterrupt, SystemExit):
	sense.clear()
	print('\n' + 'Stopped ColorPicker')
	sys.exit(0)