from sense_hat import SenseHat
import sqlite3
import datetime
import time

sense = SenseHat()

sqlite_file = "sensor_data.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

for i in range(1,1000):
    measure_time = datetime.datetime.utcnow()
    
    pressure = sense.get_pressure()
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (1, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(pressure, measure_time)
    c.execute(query)
    conn.commit()
    
    humidity = sense.get_humidity()      
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (2, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(humidity, measure_time)
    c.execute(query)
    conn.commit()
    
    temperature = sense.get_temperature()    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (3, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(temperature, measure_time)
    c.execute(query)
    conn.commit()
    
    magnetometer = sense.get_compass()    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (4, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(magnetometer, measure_time)
    c.execute(query)
    conn.commit()
    
    accelerometer = sense.get_accelerometer_raw()        
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (5, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(accelerometer['x'], measure_time)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (6, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(accelerometer['y'], measure_time)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (7, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(accelerometer['z'], measure_time)
    c.execute(query)
    conn.commit()
    
    gyroscope = sense.get_gyroscope_raw()    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (8, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(gyroscope['x'], measure_time)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (9, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(gyroscope['y'], measure_time)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (10, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(gyroscope['z'], measure_time)
    c.execute(query)
    conn.commit()
    
    orientation = sense.get_orientation()    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (11, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(orientation['pitch'], measure_time)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (12, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(orientation['roll'], measure_time)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (13, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(orientation['yaw'], measure_time)
    c.execute(query)
    time.sleep(1)
    conn.commit()
    
conn.close()