# Deliverables Session 05 - Rafael Antonio Echevarria Silva
# Exercise 6: Filters
from sense_hat import SenseHat
from flask import Flask, jsonify, request
import sqlite3

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

sense = SenseHat()
app = Flask(__name__)

@app.route('/database/Filtro', methods=['GET']) #http://127.0.0.1:5000/database/Filtro?from=2025-05-20%2017:50%&to=2025-05-20%2017:55%
def sensor_filtro():
    try:
        
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        
        conn = sqlite3.connect(FILE_SQL)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute(f'PRAGMA TABLE_INFO(measures)')
        info = c.fetchall()
        if not info:
            return jsonify({'error': f'Table "measures" not found'}), 404

        c.execute(f'SELECT * FROM measures WHERE date like "{from_date}" OR date like "{to_date}";')
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