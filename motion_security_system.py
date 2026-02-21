import random
import time

def detect_motion():
    """
    Simulate PIR motion detection
    """
    return random.choice([True, False])


def send_alert():
    """
    Simulate sending alert notification
    """
    print("🚨 Motion Detected!")
    print("Sending alert to homeowner...")
    print("Alert sent successfully!\n")


def security_system():
    print("Smart Security System Activated...\n")

    for i in range(5):  # 5 checks for demo
        motion = detect_motion()

        if motion:
            send_alert()
        else:
            print("No motion detected.\n")

        time.sleep(2)


if __name__ == "__main__":
    security_system()