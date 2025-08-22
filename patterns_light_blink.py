import RPi.GPIO as GPIO        #type:ignore
import time
import random

GPIO.setmode(GPIO.BOARD)

pins = [3, 5, 7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37]
num_pins = len(pins)

for pin in pins: 
    GPIO.setup(pin, GPIO.OUT)

def turn_all_off():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def sequential_chase(speed=0.1):
    print("Sequential Chase Pattern")
    for _ in range(1):  
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(speed)
            GPIO.output(pin, GPIO.LOW)
        for pin in reversed(pins):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(speed)
            GPIO.output(pin, GPIO.LOW)
    turn_all_off()

def alternate_blink(speed=0.5):
    print("Alternate Blink Pattern")
    for _ in range(1):  
        for i, pin in enumerate(pins):
            GPIO.output(pin, GPIO.HIGH if i % 2 == 0 else GPIO.LOW)
        time.sleep(speed)
        for i, pin in enumerate(pins):
            GPIO.output(pin, GPIO.LOW if i % 2 == 0 else GPIO.HIGH)
        time.sleep(speed)
    turn_all_off()

def knight_rider_scanner(speed=0.05):
    print("Knight Rider Scanner Pattern")
    for _ in range(1):        
        # Scan left to right
        for i in range(num_pins):
            turn_all_off()
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(speed)
        # Scan right to left
        for i in range(num_pins - 2, -1, -1):
            turn_all_off()
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(speed)
    turn_all_off()

def random_sparkle(iterations=50, speed=0.05):
    print("Random Sparkle Pattern")
    for _ in range(iterations):
        for pin in pins:
            GPIO.output(pin, random.choice([GPIO.LOW, GPIO.HIGH]))
        time.sleep(speed)
    turn_all_off()

# this consumes me a lot of time (keep it commented), goes through each once, gets slower with time
def binary_counter(speed=1):
    '''print("Binary Counter Pattern")
    max_count = 2 ** num_pins
    for num in range(max_count):
        for i, pin in enumerate(pins):
            GPIO.output(pin, (num >> i) & 1)
        time.sleep(speed/100)
    turn_all_off()'''
    pass

def heartbeat_blink(speed=0.2):
    print("Heartbeat Blink Pattern")
    for _ in range(1):  
        turn_all_off()
        time.sleep(speed)
        # Quick double blink
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        turn_all_off()
        time.sleep(0.1)
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        turn_all_off()
        time.sleep(speed * 2)
    turn_all_off()

def wave_pattern(speed=0.1):
    print("Wave Pattern")
    for _ in range(1):  
        # Building up the wave
        for i in range(num_pins):
            GPIO.output(pins[i], GPIO.HIGH)
            time.sleep(speed)
        # Fading out the wave
        for i in range(num_pins):
            GPIO.output(pins[i], GPIO.LOW)
            time.sleep(speed)
    turn_all_off()

try:
    print("Blinking the whole board with awesome patterns... Press Ctrl+C to stop")
    while True:
        sequential_chase()
        alternate_blink()
        knight_rider_scanner()
        random_sparkle()
        binary_counter()
        heartbeat_blink()
        wave_pattern()

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    turn_all_off()
    GPIO.cleanup()
