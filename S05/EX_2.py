# Deliverables Session 05 - Rafael Antonio Echevarria Silva
# Exercise 2: Read sensors on demand
from flask import Flask, jsonify
from sense_hat import SenseHat
import datetime

sense = SenseHat()
app = Flask(__name__)

#Read temperature and return as a formatted string.
@app.route('/temperature')
def read_temperature():
    temperature = sense.get_temperature()
    reading_time = datetime.datetime.now()
    response = "{0:%Y-%m-%d %H:%M:%S.%f},{1}\n".format(reading_time, temperature)
    return response

#Read temperature and return as JSON.
@app.route('/temperature/json')
def read_temperature_json():
    data = {}
    data ['temperature'] = sense.get_temperature()
    data ['reading_time'] = datetime.datetime.utcnow()
    return jsonify(data)

# Read sensors on demand
@app.route('/sensors/<name>')
def sensors(name):
    data = {}
    if name == 'timestamp':
        data['timestamp'] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
    elif name == 'temperature':
        data['temperature'] = sense.get_temperature()
    elif name == 'accelerometer':
        data['accelerometer'] = sense.get_accelerometer_raw()
    elif name == 'gyroscope':
        data['gyroscope'] = sense.get_gyroscope_raw()
    elif name == 'compass':
        data['compass'] = sense.get_compass()
    else:
        return jsonify({'error': 'Sensor not found'}), 404
    return jsonify(data)

if __name__ == '__main__':
 app.run(debug=True, port=5000)