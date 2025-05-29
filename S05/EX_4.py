# Deliverables Session 05 - Rafael Antonio Echevarria Silva
# Exercise 4: Error handling
from flask import Flask, jsonify, request
from sense_hat import SenseHat

sense = SenseHat()
app = Flask(__name__)

@app.route('/screen/pixel') 
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

@app.errorHandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
 app.run(debug=True, port=5000)