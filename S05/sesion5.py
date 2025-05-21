from sense_hat import SenseHat
from flask import Flask, jsonify, request
import datetime

sense = SenseHat()

app = Flask(__name__)
@app.route('/')

def main_route():
    return 'ICT: Raspberry PI SenseHat API'

#SESSION 2.A DEL PDF

#@app.route('/temperature')

# def read_temperature():
# #     temperature = sense.get_temperature()
# #     reading_time = datetime.datetime.utcnow()
# #     response = "{0:%Y-%m-%d %H:%M:%S.%f},{1}\n".format(reading_time, temperature)
# #     return response
#     data = {}
#     data ['temperature'] = sense.get_temperature()
#     data ['reading_time'] = datetime.datetime.utcnow()
#     return jsonify(data)
# 

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

@app.route('/screen/pixel') #http://<your_IP_address>/screen/pixel?x=2&y=4&color=(255,255,0)
def print_pixel():
    x = request.args.get('x')
    y = request.args.get('y')
    color = request.args.get('color')
    r,g,b = color.replace('(','').replace(')','').split(',')
    x = int(x)
    y = int(y)
    r = int(r)
    g = int(g)
    b = int(b)
    sense.set_pixel(x, y, r, g, b)
    return jsonify({})
    