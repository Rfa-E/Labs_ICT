# Deliverables Session 05 - Rafael Antonio Echevarria Silva
# Exercise 3: Write data into sense HAT
from flask import Flask, jsonify, request
from sense_hat import SenseHat

sense = SenseHat()
app = Flask(__name__)

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

if __name__ == '__main__':
 app.run(debug=True, port=5000)