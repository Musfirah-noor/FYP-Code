import random
import time
from datetime import datetime

LOG_FILE = "sensor_log.txt"

def get_sensor_data():
    """
    Simulate temperature and humidity values
    """
    temperature = random.randint(18, 40)
    humidity = random.randint(30, 80)
    return temperature, humidity


def check_alerts(temperature):
    """
    Check if temperature exceeds safe limit
    """
    if temperature > 35:
        return "⚠️ High Temperature Alert!"
    else:
        return "Normal"


def save_data(temp, hum, status):
    """
    Save sensor data into a text file
    """
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} | Temp: {temp}°C | Humidity: {hum}% | Status: {status}\n")


def main():
    print("Smart Sensor Monitoring System Started...\n")
    
    for i in range(5):  # 5 readings for demo
        temp, hum = get_sensor_data()
        status = check_alerts(temp)
        
        print(f"Reading {i+1}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {hum}%")
        print(f"Status: {status}")
        print("-" * 40)
        
        save_data(temp, hum, status)
        time.sleep(2)


if __name__ == "__main__":
    main()