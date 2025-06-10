from sense_hat import SenseHat
import sqlite3
import datetime
import time

sense = SenseHat()

sqlite_file = "Project.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

interval = 1 # seconds
i = 0 #contador de iteraciones
start_time = time.time()

def is_night(hour):
    return hour >= 20 or hour < 7

while True:
    current_time = time.time()
    measure_time = datetime.datetime.utcnow()
    local_time = datetime.datetime.now()
    hour = local_time.hour
    
    pressure = sense.get_pressure()  
    humidity = sense.get_humidity()           
    temperature = sense.get_temperature()
        
    c.execute("INSERT INTO measures (variable_id, measure, date) VALUES (1, ?, ?)",(pressure, measure_time))
    c.execute("INSERT INTO measures (variable_id, measure, date) VALUES (2, ?, ?)",(humidity, measure_time))
    c.execute("INSERT INTO measures (variable_id, measure, date) VALUES (3, ?, ?)",(temperature, measure_time))
    conn.commit()
    
    # Determinar mensaje según condiciones
    if temperature < 5:
        message = "ICE: mandatory use of tire chains"
    elif temperature > 35:
        message = "Temperature is more higher"
    elif humidity > 80 and pressure < 900:
        message = "Drive carefully, it can rain any moment"
    else:
        message = "have a nice trip"

        # Mostrar mensaje si es horario nocturno
    if is_night(hour):
        sense.low_light = True
    else:
        sense.low_light = False
    
    c.execute("INSERT INTO messages (message, date, modify) VALUES (?, ?, 0)",(message, measure_time))
    sense.show_message(message, scroll_speed=0.05, text_colour=[255, 255, 255])
        
    i += 1
    next_sample_time = start_time + i * interval
    sleep_time = max(0, next_sample_time - time.time())
    time.sleep(sleep_time)
    conn.commit()
    
conn.close()
