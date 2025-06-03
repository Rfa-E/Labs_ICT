from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

import random
import platform

class FakeSenseHat:
    def get_temperature(self):
        return round(random.uniform(15, 35), 2)

    def get_humidity(self):
        return round(random.uniform(30, 80), 2)

    def get_pressure(self):
        return round(random.uniform(980, 1050), 2)

    def get_orientation(self):
        return {
            "pitch": random.uniform(0, 360),
            "roll": random.uniform(0, 360),
            "yaw": random.uniform(0, 360)
        }

    def show_message(self, message, scroll_speed=0.05):
        print(f"[SIMULADO] Mostrar mensaje en la matriz LED: {message}")

# Usa SenseHat real si estás en Raspberry Pi, si no, usa fake
if platform.system() == 'Linux' and 'arm' in platform.machine():
    from sense_hat import SenseHat
    sense = SenseHat()
else:
    print("ℹ️ Usando simulación de Sense HAT.")
    sense = FakeSenseHat()


vms_message = "¡Bienvenidos al VMS!"

sensor_variables = {
    "temperatura": lambda: round(sense.get_temperature(), 2),
    "humedad": lambda: round(sense.get_humidity(), 2),
    "presion": lambda: round(sense.get_pressure(), 2),
    "orientacion": lambda: sense.get_orientation()
}

def good_day_to_ride(temp, humidity, pressure):
    return (
        15 <= temp <= 30 and
        30 <= humidity <= 70 and
        1000 <= pressure <= 1030
    )

@app.route("/", methods=["GET", "POST"])
def main():
    global vms_message

    if request.method == "POST":
        new_message = request.form.get("new_message")
        if new_message:
            vms_message = new_message
            sense.show_message(vms_message, scroll_speed=0.05)

    # Current sensor values
    temp = sensor_variables["temperatura"]()
    humidity = sensor_variables["humedad"]()
    pressure = sensor_variables["presion"]()

    # Recommendation
    recommendation = "¡Es un buen día para ir en moto!" if good_day_to_ride(temp, humidity, pressure) \
        else "Fijo que si sales te caes."

    return render_template("main.html",
                           group_name="Grupo D606",
                           message=vms_message,
                           date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                           variables=sensor_variables.keys(),
                           recommendation=recommendation)

@app.route("/variable/<variable_id>")
def variable_page(variable_id):
    if variable_id in sensor_variables:
        value = sensor_variables[variable_id]()
        return render_template("variable.html", variable=variable_id, value=value)
    else:
        return "Variable no encontrada", 404

@app.route("/live/<variable_id>")
def live_sensor(variable_id):
    if variable_id in sensor_variables:
        return {variable_id: sensor_variables[variable_id]()}
    else:
        return {"error": "ID de variable inválido"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

