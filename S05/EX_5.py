# Deliverables Session 05 - Rafael Antonio Echevarria Silva
# Exercise 5: Access database
from sense_hat import SenseHat
from flask import Flask, jsonify
import sqlite3

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

sense = SenseHat()
app = Flask(__name__)

@app.route('/database/<name>', methods=['GET'])
def sensor_data(name):
    try:
        TABLE_NAME = name
        conn = sqlite3.connect(FILE_SQL)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute(f'PRAGMA TABLE_INFO({TABLE_NAME})')
        info = c.fetchall()
        if not info:
            return jsonify({'error': f'Table "{TABLE_NAME}" not found'}), 404

        c.execute(f'SELECT * FROM {TABLE_NAME}')
        rows = c.fetchall()

        result = [dict(row) for row in rows]

        conn.close()
        return jsonify({
            "columns": [col[1] for col in info],
            "data": result
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
 app.run(debug=True, port=5000)