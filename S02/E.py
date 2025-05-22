# Deliverables Session 02 - Rafael Antonio Echevarria Silva

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

n = 10

# E. (0,75) To calculate the computation time without using “print” for show sensor information in the screen

for i in range(n):
    
    start_time = time.perf_counter()  # Start timer

    temp = round(sense.get_temperature(), 1)
    pres = round(sense.get_pressure(), 1)
    hum = round(sense.get_humidity(), 1)
    
    north = sense.get_compass()
    magneto = sense.get_compass_raw()
    gyro = sense.get_gyroscope_raw()
    accel = sense.get_accelerometer_raw()
    orientation = sense.get_orientation()
    
    # Here we are not printing the values to the screen, just calculating the time taken for each sensor reading
    end_time = time.perf_counter()  # End timer
    elapsed_time = end_time - start_time
    print(f"Computation Time: {elapsed_time:.4f} seconds")
    print("-" * 50)
    
    sense.clear()