import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pin for LED
PIN_SELECTED = 18

# Set up the LED pin as output
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
    # Clean up GPIO on Ctrl+C
    print("\nProgram terminated")
    GPIO.cleanup()