# Deliverables Session 02 - Rafael Antonio Echevarria Silva

from sense_hat import SenseHat
from datetime import datetime
import time
import csv

sense = SenseHat()
sense.clear()

n = 10

# I. (0,5) To write sensor information in a “.csv” file, but using a file for each sensor

files = {
    'temperature': 'temperature.csv',
    'pressure': 'pressure.csv',
    'humidity': 'humidity.csv',
    'compass': 'compass.csv',
    'magnetometer': 'magnetometer.csv',
    'gyroscope': 'gyroscope.csv',
    'accelerometer': 'accelerometer.csv',
    'orientation': 'orientation.csv'
}

headers = {
    'temperature': ['Timestamp', 'Temperature (C)'],
    'pressure': ['Timestamp', 'Pressure (hPa)'],
    'humidity': ['Timestamp', 'Humidity (%)'],
    'compass': ['Timestamp', 'North (°)'],
    'magnetometer': ['Timestamp', 'X', 'Y', 'Z'],
    'gyroscope': ['Timestamp', 'X', 'Y', 'Z'],
    'accelerometer': ['Timestamp', 'X', 'Y', 'Z'],
    'orientation': ['Timestamp', 'Pitch', 'Roll', 'Yaw']
}

for sensor, filename in files.items():
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers[sensor])

for i in range(n):

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    #print(f"Timestamp: {timestamp}")
    
    temp = round(sense.get_temperature(), 1)
    pres = round(sense.get_pressure(), 1)
    hum = round(sense.get_humidity(), 1)
    
    #print("Temperature: {0} C".format(temp) + " Pressure: {0} hPa".format(pres) + " Humidity: {0} %".format(hum))
    #print("-" * 50)

    north = sense.get_compass()
    #print(f"North: {north:.2f}°")
    
    magneto = sense.get_compass_raw()
    #print(f"Magnetometer: x={magneto['x']:.2f}, y={magneto['y']:.2f}, z={magneto['z']:.2f}")
   
    gyro = sense.get_gyroscope_raw()
    #print(f"Gyroscope: x={gyro['x']:.2f}, y={gyro['y']:.2f}, z={gyro['z']:.2f}")
    
    accel = sense.get_accelerometer_raw()
    #print(f"Accelerometer: x={accel['x']:.2f}, y={accel['y']:.2f}, z={accel['z']:.2f}")
    
    orientation = sense.get_orientation()
    #print(f"Orientation: pitch={orientation['pitch']:.2f}, roll={orientation['roll']:.2f}, yaw={orientation['yaw']:.2f}")
    
    with open(files['temperature'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, temp])

    with open(files['pressure'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, pres])

    with open(files['humidity'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, hum])

    with open(files['compass'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, north])

    with open(files['magnetometer'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, round(magneto['x'], 2), round(magneto['y'], 2), round(magneto['z'], 2)])

    with open(files['gyroscope'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, round(gyro['x'], 2), round(gyro['y'], 2), round(gyro['z'], 2)])

    with open(files['accelerometer'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, round(accel['x'], 2), round(accel['y'], 2), round(accel['z'], 2)])

    with open(files['orientation'], 'a', newline='') as f:
        csv.writer(f).writerow([timestamp, round(orientation['pitch'], 2), round(orientation['roll'], 2), round(orientation['yaw'], 2)])
    
    print("-" * 50)
    time.sleep(1)
    sense.clear()