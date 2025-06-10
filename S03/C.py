# Deliverables Session 03 - Rafael Antonio Echevarria Silva
# A. Create a database

from sense_hat import SenseHat
import sqlite3

sense = SenseHat()

sqlite_file = "sensor_data.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#PRACTICE 2.A
#Creating a new SQLite table for sensors
c.execute("CREATE TABLE sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, virtual INTEGER)")
#Creating a new table for variables
c.execute("CREATE TABLE variables (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_id INTEGER, name TEXT NOT NULL, description TEXT, units TEXT)")
#Creating a new table for measures
c.execute("CREATE TABLE measures (id INTEGER PRIMARY KEY AUTOINCREMENT, variable_id INTEGER, measure REAL, date TEXT)")

#PRACTICE 2.B
sensors = [
    # (name, description, virtual)
    ("temperature", "Temperature sensor", 0),
    ("pressure",    "Pressure sensor",    0),
    ("humidity",    "Humidity sensor",    0),
    ('Accelerometer', 'Accelerometer sensor', 0),
    ('Magnetometer', 'Magnetometer sensor', 0),
    ('Gyroscope', 'Gyroscope sensor', 0),
    ('Orientation', 'Orientation sensor', 0)
    ]

for name, desc, virt in sensors:
    c.execute("INSERT INTO sensors (name, description, virtual) VALUES (?, ?, ?)",(name, desc, virt))

variables = [
    # (sensor_id, nombre, descripción, unidades)
    ('1','Pressure', 'Pressure sensor', 'Pa'),
    ('2','Humidity', 'Humidity sensor', '%'),
    ('3','Temperature', 'Temperature sensor', 'ºC'),
    ('4','Magnetometer', 'Magnetometer sensor', 'Gauss'),
    ('5','X', 'Accelerometer sensor', 'm/s'),
    ('5','Y', 'Accelerometer sensor', 'm/s'),
    ('5','Z', 'Accelerometer sensor', 'm/s'),
    ('6','X', 'Gyroscope sensor', 'rad'),
    ('6','Y', 'Gyroscope sensor', 'rad'),
    ('6','Z', 'Gyroscope sensor', 'rad'),
    ('7','pitch', 'Orientation sensor', 'º'),
    ('7','roll', 'Orientation sensor', 'º'),
    ('7','yaw', 'Orientation sensor', 'º')
    ]

for sensor_id, name, desc, units in variables:
    c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES (?, ?, ?, ?)",(sensor_id, name, desc, units))

conn.commit()
conn.close()