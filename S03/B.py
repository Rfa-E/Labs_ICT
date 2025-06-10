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

conn.commit()
conn.close()