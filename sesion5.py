from sense_hat import SenseHat
from flask import Flask


sense = SenseHat()

app = Flask(__name__)
@app.route('/temperature')

def read_temperature():
    temperature = sense.get_temperature()
    reading_time = datetime.datetime.utcnow()
    response = "{0:%Y-%m-%d %H:%M:%S.%f},{1}\n".format(reading_time, temperature)
    return response

# def main_route():
#     return 'ICT: Raspberry PI SenseHat API'
