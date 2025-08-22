#use the code in a raspberry pi GPIO compiler
#https://create.withcode.uk/python/A5


import RPi.GPIO as GPIO #type:ignore
import time


GPIO.setmode(GPIO.BCM)

PIN_SELECTED = 18

GPIO.setup(PIN_SELECTED, GPIO.OUT)

try:
    while True:
        # Turn LED on
        GPIO.output(PIN_SELECTED, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # Wait for 1 second
        
        # Turn LED off
        GPIO.output(PIN_SELECTED, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    
    print("\nProgram terminated")
    GPIO.cleanup()