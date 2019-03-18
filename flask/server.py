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

# Define the root route
@app.route('/')
def index():
  return 'Look the flask server is running'

# Define the my_ip route
@app.route('/my_ip', methods=['GET'])
def my_ip():
  return jsonify({
    'ip': request.remote_addr
  }), 200
    
# Utilities
hex2rgb = lambda hx: (int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))
# Define the api_environment route
@app.route('/environment', methods=['GET', 'POST'])
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

  data = request.form

  
  if data:
    color = (hex2rgb(data['hexColor']))
    print(color)
    sense.clear(color)
    
  return render_template('index.html', environment=environment_obj, data=data)

# Main method for Flask server
if __name__ == '__main__':
  app.run(host = '192.168.5.198', port = 8080, debug = True)