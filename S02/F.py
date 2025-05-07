# Deliverables Session 02 - Rafael Antonio Echevarria Silva

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

n = 10 # Number of readings to be taken

# F. (1) To obtain the “sample frequency” for each sensor

for i in range(n):
    
    start_temp = time.time()  # Start timer
    temp = round(sense.get_temperature(), 1)
    end_temp = time.time()  # End timer
    elapsed_temp = end_temp - start_temp
    freq_temp = 1 / elapsed_temp if elapsed_temp != 0 else float('inf')
    print(f"Temperature: {temp} °C, Sample Frequency: {freq_temp:.2f} Hz")
    
    start_press = time.time()  # Start timer
    press = round(sense.get_pressure(), 1)
    end_press = time.time()  # End timer
    elapsed_press = end_press - start_press
    freq_temp = 1 / elapsed_press if elapsed_press != 0 else float('inf')
    print(f"Pressure: {press} hPa, Sample Frequency: {freq_temp:.2f} Hz")
    
    start_hum = time.time()  # Start timer
    hum = round(sense.get_humidity(), 1)
    end_hum = time.time()  # End timer
    elapsed_hum = end_hum - start_hum
    freq_temp = 1 / elapsed_hum if elapsed_hum != 0 else float('inf')
    print(f"Humidity: {hum} %, Sample Frequency: {freq_temp:.2f} Hz")

    # With this function we can calculate the sample frequency
    # of the accelerometer, gyroscope and magnetometer    
    start_IMU = time.time()  # Start timer
    # Read all sensors
    north = sense.get_compass()
    magneto = sense.get_compass_raw()
    gyro = sense.get_gyroscope_raw()
    accel = sense.get_accelerometer_raw()
    orientation = sense.get_orientation()
    end_IMU = time.time()  # End timer
    elapsed_IMU = end_IMU - start_IMU
    freq_IMU = 1 / elapsed_IMU if elapsed_IMU != 0 else float('inf')
    print(f"IMU Data: {orientation}, Sample Frequency: {freq_IMU:.2f} Hz")
    
    print("-" * 50)
    
    time.sleep(1) # Sleep for 1 second
    sense.clear()