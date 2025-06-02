# Deliverables Session 06 - Rafael Antonio Echevarria Silva
# Exercise 3: Write new endpoint /sensors that renders a template that shows a table with the sensors available on the DB
# • Table with sensors on the db
# • Table should have table headers 
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

@app.route('/')
def main():
   return render_template('main.html')

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
