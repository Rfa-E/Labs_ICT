# Deliverables Session 02 - Rafael Antonio Echevarria Silva

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

n = 10 

# C. (1) Use a loop for reading sensor information

for i in range(n):

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
    sense.clear()