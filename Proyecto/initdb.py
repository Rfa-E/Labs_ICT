from sense_hat import SenseHat
import sqlite3
import datetime
import time

sense = SenseHat()

sqlite_file = "Project.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#PRACTICE 2.A
#Creating a new SQLite table for sensors
c.execute("CREATE TABLE sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, virtual INTEGER)")
#Creating a new table for variables
c.execute("CREATE TABLE variables (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_id INTEGER, name TEXT NOT NULL, description TEXT, units TEXT)")
#Creating a new table for measures
c.execute("CREATE TABLE measures (id INTEGER PRIMARY KEY AUTOINCREMENT, variable_id INTEGER, measure REAL, date TIMESTAMP)")

c.execute("CREATE TABLE messages (message TEXT NOT NULL, date TIMESTAMP NOT NULL, modify BIT NOT NULL, PRIMARY KEY(date))")

#PRACTICE 2.B
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Pressure', 'Pressure sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Humidity', 'Humidity sensor', 0)")
c.execute("INSERT INTO sensors (name, description, virtual) VALUES ('Temperature', 'Temperature sensor', 0)")

#PRACTICE 2.C
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('1','Pressure', 'Pressure sensor', 'Pa')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('2','Humidity', 'Humidity sensor', '%')")
c.execute("INSERT INTO variables (sensor_id, name, description, units) VALUES ('3','Temperature', 'Temperature sensor', 'ºC')")

conn.commit()
conn.close()
