from sense_hat import SenseHat
from flask import Flask, jsonify, request
import sqlite3

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

sense = SenseHat()
app = Flask(__name__)

@app.route('/')
def main_route():
    return 'ICT: Raspberry PI SenseHat API'

@app.route('/database/<name>', methods=['GET'])
def sensor_data(name):
    try:
        TABLE_NAME = name
        conn = sqlite3.connect(FILE_SQL)
        conn.row_factory = sqlite3.Row  # This allows us to access columns by name
        c = conn.cursor()

        # Check if table exists
        c.execute(f'PRAGMA TABLE_INFO({TABLE_NAME})')
        info = c.fetchall()
        if not info:
            return jsonify({'error': f'Table "{TABLE_NAME}" not found'}), 404

        # Fetch all rows
        c.execute(f'SELECT * FROM {TABLE_NAME}')
        rows = c.fetchall()

        # Convert each row to a dictionary
        result = [dict(row) for row in rows]

        conn.close()
        return jsonify({
            "columns": [col[1] for col in info],
            "data": result
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/database/Filtro', methods=['GET'])
def sensor_filtro():
    try:
        
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        
        conn = sqlite3.connect(FILE_SQL)
        conn.row_factory = sqlite3.Row  # This allows us to access columns by name
        c = conn.cursor()

        # Check if table exists
        c.execute(f'PRAGMA TABLE_INFO(measures)')
        info = c.fetchall()
        if not info:
            return jsonify({'error': f'Table "measures" not found'}), 404

        # Fetch all rows
        c.execute(f'SELECT * FROM measures WHERE date like "{from_date}" OR date like "{to_date}";') #http://127.0.0.1:5000/database/Filtro?from=2025-05-20%2017:50%&to=2025-05-20%2017:55%
        rows = c.fetchall()

        # Convert each row to a dictionary
        result = [dict(row) for row in rows]

        conn.close()
        return jsonify({
            "columns": [col[1] for col in info],
            "data": result
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
