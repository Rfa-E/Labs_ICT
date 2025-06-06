# Deliverables Session 02 - Rafael Antonio Echevarria Silva

from sense_hat import SenseHat
from datetime import datetime
import time
import csv

sense = SenseHat()
sense.clear()

n = 10
csv_filename = "sensor_data.csv"

# H. (1,5) To write sensor information in a common “.csv” file

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Time", "Temp (C)", "Pressure (hPa)", "Humidity (%)", 
        "North (°)", 
        "Magneto X", "Magneto Y", "Magneto Z",
        "Gyro X", "Gyro Y", "Gyro Z",
        "Accel X", "Accel Y", "Accel Z",
        "Pitch", "Roll", "Yaw"
    ])

for i in range(n):

    # Get current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"Timestamp: {timestamp}")
    
    temp = round(sense.get_temperature(), 1)
    pres = round(sense.get_pressure(), 1)
    hum = round(sense.get_humidity(), 1)
    
    print("Temperature: {0} C".format(temp) + " Pressure: {0} hPa".format(pres) + " Humidity: {0} %".format(hum))
    print("-" * 50)

    north = sense.get_compass()
    print(f"North: {north:.2f}°")
    
    magneto = sense.get_compass_raw()
    print(f"Magnetometer: x={magneto['x']:.2f}, y={magneto['y']:.2f}, z={magneto['z']:.2f}")
   
    gyro = sense.get_gyroscope_raw()
    print(f"Gyroscope: x={gyro['x']:.2f}, y={gyro['y']:.2f}, z={gyro['z']:.2f}")
    
    accel = sense.get_accelerometer_raw()
    print(f"Accelerometer: x={accel['x']:.2f}, y={accel['y']:.2f}, z={accel['z']:.2f}")
    
    orientation = sense.get_orientation()
    print(f"Orientation: pitch={orientation['pitch']:.2f}, roll={orientation['roll']:.2f}, yaw={orientation['yaw']:.2f}")
    
    print("-" * 50)
    
    writer.writerow([
            timestamp, temp, pres, hum,
            north,
            round(magneto['x'], 2), round(magneto['y'], 2), round(magneto['z'], 2),
            round(gyro['x'], 2), round(gyro['y'], 2), round(gyro['z'], 2),
            round(accel['x'], 2), round(accel['y'], 2), round(accel['z'], 2),
            round(orientation['pitch'], 2), round(orientation['roll'], 2), round(orientation['yaw'], 2)
        ])
    
    sense.clear()