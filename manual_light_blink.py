import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_SELECTED = 18

GPIO.setup(PIN_SELECTED, GPIO.OUT)

def start_blinking():
    print("Starting automatic blink mode. Press Ctrl+C to return to manual control.")
    try:
        while True:
            # Turn LED on
            GPIO.output(PIN_SELECTED, GPIO.HIGH)
            print("LED ON")
            time.sleep(1)              
            # Turn LED off
            GPIO.output(PIN_SELECTED, GPIO.LOW)
            print("LED OFF")
            time.sleep(1)     
    except KeyboardInterrupt:
        print("\nBlinking stopped. Returning to manual mode.")
        GPIO.output(PIN_SELECTED, GPIO.LOW) k

try:
    print("LED Control Program")
    print("Commands: 'on' - Turn LED on")
    print("         'off' - Turn LED off")
    print("         'blink' - Start automatic blinking")
    print("         'quit' - Exit the program")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'on':
            GPIO.output(PIN_SELECTED, GPIO.HIGH)
            print("LED turned ON manually")
        
        elif command == 'off':
            GPIO.output(PIN_SELECTED, GPIO.LOW)
            print("LED turned OFF manually")
        
        elif command == 'blink':
            start_blinking()
        
        elif command == 'quit':
            print("Exiting program")
            break
        
        else:
            print("Invalid command. Try 'on', 'off', 'blink', or 'quit'.")

except KeyboardInterrupt:
    print("\nProgram terminated by user")

finally:
    GPIO.output(PIN_SELECTED, GPIO.LOW)  # Ensure LED is off
    GPIO.cleanup()
    print("GPIO cleaned up")
