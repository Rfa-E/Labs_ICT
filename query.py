from sense_hat import SenseHat
import sqlite3
import datetime
import time

sense = SenseHat()

sqlite_file = "sensor_data.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

for i in range(1,5):
    pressure = sense.get_pressure()
    measure_time = datetime.datetime.utcnow()
    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (1, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(pressure, measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()
    

for i in range(1,5):
    humidity = sense.get_humidity()
    measure_time = datetime.datetime.utcnow()
    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (2, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(humidity, measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()
    
for i in range(1,5):
    temperature = sense.get_temperature()
    measure_time = datetime.datetime.utcnow()
    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (3, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(temperature, measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()

for i in range(1,5):
    magnetometer = sense.get_compass()
    measure_time = datetime.datetime.utcnow()
    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (4, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(magnetometer, measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()
    
for i in range(1,5):
    accelerometer = sense.get_accelerometer_raw()
    measure_time = datetime.datetime.utcnow()
        
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (5, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(accelerometer['x'], measure_time)
    print(query)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (6, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(accelerometer['y'], measure_time)
    print(query)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (7, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(accelerometer['z'], measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()
    
for i in range(1,5):
    gyroscope = sense.get_gyroscope_raw()
    measure_time = datetime.datetime.utcnow()
    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (8, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(gyroscope['x'], measure_time)
    print(query)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (9, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(gyroscope['y'], measure_time)
    print(query)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (10, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(gyroscope['z'], measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()
    
for i in range(1,5):
    orientation = sense.get_orientation()
    measure_time = datetime.datetime.utcnow()
    
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (11, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(orientation['pitch'], measure_time)
    print(query)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (12, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(orientation['roll'], measure_time)
    print(query)
    c.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (13, {0},'{1:%Y-%m-%d %H:%M:%S.%f}')".format(orientation['yaw'], measure_time)
    print(query)
    c.execute(query)
    time.sleep(0.2)
    conn.commit()

query = "select sensors.name, variables.name, measures.measure, max(measures.date), variables.units from sensors, variables, measures where sensors.id = variables.sensor_id and variables.id = measures.variable_id group by variables.id"
c.execute(query)
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()