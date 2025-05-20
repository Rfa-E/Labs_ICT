from sense_hat import SenseHat
import sqlite3
import datetime
import time

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
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Pressure', 'Pressure sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Humidity', 'Humidity sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Temperature', 'Temperature sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Accelerometer', 'Accelerometer sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Magnetometer', 'Magnetometer sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Gyroscope', 'Gyroscope sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Orientation', 'Orientation sensor', 0)")

#PRACTICE 2.C
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('1','Pressure', 'Pressure sensor', 'Pa')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('2','Humidity', 'Humidity sensor', '%')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('3','Temperature', 'Temperature sensor', 'ºC')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('4','Magnetometer', 'Magnetometer sensor', 'Gauss')")

c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('5','X', 'Accelerometer sensor', 'm/s')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('5','Y', 'Accelerometer sensor', 'm/s')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('5','Z', 'Accelerometer sensor', 'm/s')")


c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('6','X', 'Gyroscope sensor', 'rad')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('6','Y', 'Gyroscope sensor', 'rad')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('6','Z', 'Gyroscope sensor', 'rad')")

c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('7','pitch', 'Orientation sensor', 'º')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('7','roll', 'Orientation sensor', 'º')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('7','yaw', 'Orientation sensor', 'º')")


conn.commit()
conn.close()