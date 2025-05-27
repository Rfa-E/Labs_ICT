from sense_hat import SenseHat
from flask import Flask, jsonify, request
import datetime
import sqlite3

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

conn = sqlite3.connect(FILE_SQL)
c = conn.cursor()
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

# @app.route('/sensors/<name>')
# def sensors(name):
#     data = {}
#     if name == 'timestamp':
#         data['timestamp'] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
#     elif name == 'temperature':
#         data['temperature'] = sense.get_temperature()
#     elif name == 'accelerometer':
#         data['accelerometer'] = sense.get_accelerometer_raw()
#     elif name == 'gyroscope':
#         data['gyroscope'] = sense.get_gyroscope_raw()
#     elif name == 'compass':
#         data['compass'] = sense.get_compass()
#     else:
#         return jsonify({'error': 'Sensor not found'}), 404
#     return jsonify(data)

# @app.route('/screen/pixel') #http://<your_IP_address>/screen/pixel?x=2&y=4&color=(255,255,0)
# def print_pixel():
#     x = request.args.get('x')
#     y = request.args.get('y')
#     color = request.args.get('color')
#     r,g,b = color.replace('(','').replace(')','').split(',')
#     x = int(x)
#     y = int(y)
#     r = int(r)
#     g = int(g)
#     b = int(b)
#     sense.set_pixel(x, y, r, g, b)
#     return jsonify({})

@app.route('/sensors')
def connect(file_sql):
    conn = sqlite3.connect(file_sql)
    c = conn.cursor()
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()
    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0
    for col in col_dict:
        c.execute('SELECT ({0}) FROM {1} '
                  'WHERE {0} IS NOT NULL'.format(col, table_name))
        # In my case this approach resulted in a
        # better performance than using COUNT
        number_rows = len(c.fetchall())
        col_dict[col] = number_rows
    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))
    return conn, c, col_dict

# def close(conn):
#     # conn.commit()
#     conn.close()