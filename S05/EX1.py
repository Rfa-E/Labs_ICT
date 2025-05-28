# Deliverables Session 05 - Rafael Antonio Echevarria Silva
# Exercise 1: Create a web service with FLASK
from flask import Flask

app = Flask(__name__)

# section 1: Create a web service with FLASK
@app.route('/')
def main_route():
    return 'ICT: Raspberry PI SenseHat API'

#section 1b: Run server from Thonny without using terminal
@app.route('/hello') 
def hello_world():
 return "<p>Hello, World!</p>"

if __name__ == '__main__':
 app.run(debug=True, port=5000)