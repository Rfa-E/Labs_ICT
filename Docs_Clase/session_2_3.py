import csv
import time
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

sense.show_letter("J")

# Define filenames
temp_file = "temperature_log.csv"
hum_file = "humidity_log.csv"
press_file = "pressure_log.csv"

# Define common header
header = ["Timestamp", "Sample Frequency (Hz)", "Value"]

# Create and initialize each CSV file with header
for filename in [temp_file, hum_file, press_file]:
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

# Initialize previous time
previous_time = time.time()

# Main loop
while True:
    start_time = time.time()

    # Generate timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Read sensor values
    temp = round(sense.get_temperature(), 1)
    hum = round(sense.get_humidity(), 1)
    press = round(sense.get_pressure(), 1)

    # Calculate frequency
    current_time = time.time()
    time_diff = current_time - previous_time
    frequency = 1 / time_diff if time_diff != 0 else float('inf')
    previous_time = current_time

    # Print info
    print(f"Timestamp: {timestamp}")
    print(f"Temperature: {temp} °C, Humidity: {hum} %, Pressure: {press} hPa")
    print(f"Sample Frequency: {frequency:.2f} Hz\n")

    # Log to each file separately
    with open(temp_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, f"{frequency:.2f}", temp])

    with open(hum_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, f"{frequency:.2f}", hum])

    with open(press_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, f"{frequency:.2f}", press])

    time.sleep(0.1)

