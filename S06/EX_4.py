# Deliverables Session 06 - Rafael Antonio Echevarria Silva
# Exercise 4:
# Link all pages using <a> html links
# • Add link to /info from the main page /
# • Add link to main page / from the /info page

# Add CSS style to your webpage as you want
# ¿Can we add CSS style (color) depending on the current reading of some of the senseHAT sensors? How?

from flask import Flask, render_template, request
import sqlite3
from sense_hat import SenseHat
import random

sense = SenseHat()

def random_colour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

app = Flask(__name__)

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/hello')
def hello():
    name = request.args.get('group')
    return render_template('hello.html', name = name)

@app.route('/info/<name>', methods=['GET'])
def info(name):
    conn = sqlite3.connect(FILE_SQL)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    TABLE_NAME = name
    
    c.execute(f'PRAGMA TABLE_INFO({TABLE_NAME})')
    columns_info = c.fetchall()
    
    c.execute(f'SELECT * FROM {TABLE_NAME}')
    rows = c.fetchall()
    result = [dict(row) for row in rows]

    return render_template('info.html', columns=[col[1] for col in columns_info], data=result)