# Deliverables Session 02 - Rafael Antonio Echevarria Silva

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# A. (0,5) Reading of the sensor information:
    # a.1. Environmental sensors
    # a.1.1. Temperature
temp = round(sense.get_temperature(), 1)
    # a.1.2. Pressure
pres = round(sense.get_pressure(), 1)
    # a.1.3. Humidity
hum = round(sense.get_humidity(), 1)
    
print("Temperature: {0} C".format(temp) + " Pressure: {0} hPa".format(pres) + " Humidity: {0} %".format(hum))
print("-" * 50)
# a.2.IMU (Inertial Measurement Unit) sensors
# a.2.1. North (Compass heading)
north = sense.get_compass()
print(f"North: {north:.2f}°")
    
# a.2.2. Magnetometer
magneto = sense.get_compass_raw()
print(f"Magnetometer: x={magneto['x']:.2f}, y={magneto['y']:.2f}, z={magneto['z']:.2f}")
  
# a.2.3. Gyroscope
gyro = sense.get_gyroscope_raw()
print(f"Gyroscope: x={gyro['x']:.2f}, y={gyro['y']:.2f}, z={gyro['z']:.2f}")

# a.2.4. Accelerometer
accel = sense.get_accelerometer_raw()
print(f"Accelerometer: x={accel['x']:.2f}, y={accel['y']:.2f}, z={accel['z']:.2f}")
    
# a.2.5. Orientation
orientation = sense.get_orientation()
print(f"Orientation: pitch={orientation['pitch']:.2f}, roll={orientation['roll']:.2f}, yaw={orientation['yaw']:.2f}")
    
print("-" * 50)
sense.clear()