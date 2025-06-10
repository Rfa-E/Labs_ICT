from flask import Flask, render_template, request
from sense_hat import SenseHat
import datetime
import sqlite3

app = Flask(__name__)

sense = SenseHat()

@app.route("/probe")
def probe():
    return 'VMS is working properly'

def get_latest_message_and_conditions():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Obtener último mensaje
    c.execute("SELECT message, date FROM messages ORDER BY date DESC LIMIT 1")
    msg_row = c.fetchone()
    message = msg_row[0] if msg_row else "No hay mensajes registrados"
    msg_date = msg_row[1] if msg_row else None

    # Obtener valores asociados de cada variable en ese momento (por fecha del mensaje)
    temp = humidity = pressure = None
    if msg_date:
        for var_id, var_name in [(3, 'temp'), (2, 'humidity'), (1, 'pressure')]:
            c.execute("""
                SELECT measure FROM measures
                WHERE variable_id = ? AND ABS(julianday(date) - julianday(?)) < 0.0007
                ORDER BY ABS(julianday(date) - julianday(?)) ASC
                LIMIT 1
            """, (var_id, msg_date, msg_date))
            row = c.fetchone()
            if row:
                val = round(row[0], 2)
                if var_id == 3:
                    temp = val
                elif var_id == 2:
                    humidity = val
                elif var_id == 1:
                    pressure = val

    conn.close()
    return message, msg_date, temp, humidity, pressure

def get_variable_unit(variable_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT units FROM variables WHERE id = ?", (variable_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else ""

def get_latest_value(variable_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT measure FROM measures WHERE variable_id = ? ORDER BY date DESC LIMIT 1", (variable_id,))
    row = c.fetchone()
    conn.close()
    return round(row[0], 2) if row else None

sensor_variables = {
    "temperatura": lambda: get_latest_value(3),
    "humedad": lambda: get_latest_value(2),
    "presion": lambda: get_latest_value(1)
}

@app.route("/", methods=["GET", "POST"])
def main():
    global vms_message

    # Obtener valores actuales ANTES de posible mensaje nuevo
    latest_pressure = get_latest_value(1)
    latest_humidity = get_latest_value(2)
    latest_temp = get_latest_value(3)

    if request.method == "POST":
        new_message = request.form.get("new_message")
        if new_message:
            vms_message = new_message
            sense.show_message(vms_message, scroll_speed=0.05)

            # Guardar nuevo mensaje en la base de datos con la hora actual UTC
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            current_time = datetime.datetime.utcnow()
            c.execute("INSERT INTO messages (message, date, modify) VALUES (?, ?, 1)", (vms_message, current_time))
            c.execute("INSERT INTO measures (variable_id, measure, date) VALUES (1, ?, ?)", (latest_pressure, current_time))
            c.execute("INSERT INTO measures (variable_id, measure, date) VALUES (2, ?, ?)", (latest_humidity, current_time))
            c.execute("INSERT INTO measures (variable_id, measure, date) VALUES (3, ?, ?)", (latest_temp, current_time))
            conn.commit()
            conn.close()

    # Obtener el último mensaje y condiciones asociadas
    db_message, message_time, temp, humidity, pressure = get_latest_message_and_conditions()
    vms_message = db_message

    # Obtener unidades desde la base de datos
    temp_unit = get_variable_unit(3)
    humidity_unit = get_variable_unit(2)
    pressure_unit = get_variable_unit(1)

    # Preparar salida para mostrar "N/A" si no hay datos
    temp_disp = f"{temp} {temp_unit}" if temp is not None else "N/A"
    humidity_disp = f"{humidity} {humidity_unit}" if humidity is not None else "N/A"
    pressure_disp = f"{pressure} {pressure_unit}" if pressure is not None else "N/A"

    return render_template("main.html",
                           group_name="Grupo D606",
                           message=vms_message,
                           date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                           variables=sensor_variables.keys(),
                           temp=temp_disp,
                           humidity=humidity_disp,
                           pressure=pressure_disp)

@app.route("/variable/<variable_id>")
def variable_page(variable_id):
    if variable_id in sensor_variables:
        value = sensor_variables[variable_id]()
        unit = get_variable_unit({"temperatura": 3, "humedad": 2, "presion": 1}[variable_id])
        return render_template("variable.html", variable=variable_id, value=f"{value} {unit}" if value is not None else "N/A")
    else:
        return "Variable no encontrada", 404

@app.route("/live/<variable_id>")
def live_sensor(variable_id):
    if variable_id in sensor_variables:
        return {variable_id: sensor_variables[variable_id]()}
    else:
        return {"error": "ID de variable inválido"}, 404
    
@app.route("/search")
def search():
    search_date = request.args.get("date")
    results = []

    if search_date:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        # Buscar mensajes que coincidan con la fecha seleccionada
        c.execute("""
            SELECT m.message, m.date,
                (SELECT measure FROM measures WHERE variable_id = 3 AND date = m.date) as temp,
                (SELECT measure FROM measures WHERE variable_id = 2 AND date = m.date) as humidity,
                (SELECT measure FROM measures WHERE variable_id = 1 AND date = m.date) as pressure
            FROM messages m
            WHERE DATE(m.date) = ?
            ORDER BY m.date DESC
        """, (search_date,))

        rows = c.fetchall()
        conn.close()

        for row in rows:
            results.append({
                "message": row[0],
                "date": row[1],
                "temp": f"{round(row[2], 2)} {get_variable_unit(3)}" if row[2] is not None else "N/A",
                "humidity": f"{round(row[3], 2)} {get_variable_unit(2)}" if row[3] is not None else "N/A",
                "pressure": f"{round(row[4], 2)} {get_variable_unit(1)}" if row[4] is not None else "N/A",
            })

    return render_template("main.html",
                           group_name="Grupo D606",
                           message=vms_message,
                           date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                           variables=sensor_variables.keys(),
                           temp="",
                           humidity="",
                           pressure="",
                           results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
