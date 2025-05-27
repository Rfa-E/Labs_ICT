from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

FILE_SQL = '/home/pi/Downloads/sensor_data.db'

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/hello')
def hola_joao():
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

@app.route('/showtext', methods=['POST'])
def showtext():
    user_input = request.form.get('usertext')
    print(f"Received text from form: {user_input}")
    return f"<h1>You sent: {user_input}</h1><p>Check the server console for the printed text.</p>"

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)