import time
import Jetson.GPIO as GPIO

PIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
#GPIO.setup(PIR_PIN_THREE, GPIO.IN)

def detect_motion():
    time.sleep(1)
    print("찾는중..")
    if GPIO.input(PIR_PIN):
        print("감지!")
        return True
    else:
        print("감지되지 않았습니다.")
        return False
