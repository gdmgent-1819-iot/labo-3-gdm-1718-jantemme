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
from time import sleep

# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()

# Define the api_environment route
@app.route('/', methods=['GET', 'POST'])
def environment():
  environment_obj = {
    'temperature': {
      'value': round(sense.get_temperature()) - 18,
      'unit': u'°C'
    },
    'humidity': {
      'value': round(sense.get_humidity()),
      'unit': u'%'
    },
    'pressure': {
      'value': round(sense.get_pressure()),
      'unit': u'mbar'
    }
  }
    
  return render_template('index.html', environment=environment_obj)

# Main method for Flask server
if __name__ == '__main__':
  app.run(host = '192.168.5.198', port = 8082, debug = True)