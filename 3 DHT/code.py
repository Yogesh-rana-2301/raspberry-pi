import utime   #for microcontrollers
import machine #micropython microcontroller lib
import random

#ANSI color codes
RED = "\033[91m"   #escape char + code
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


#i am taking random values for the temperature and humidity in my case but if you
#want it to work on real life testing use the code in the next function docstring
def read_dht11():
    """
    connection: 
    "dht11:VCC", "pico:3V3", 
    "dht11:GND", "pico:GND.8"
    "dht11:DATA", "pico:GP22", 
    """

    temp = random.uniform(15, 40)
    hum = random.uniform(20, 90)
    alert = ""
    if temp > 35 or temp < 10:
        alert += f"{RED}⚠️ Temp Alert!{RESET} "
    if hum > 80 or hum < 20:
        alert += f"{RED}⚠️ Humidity Alert!{RESET}"

    return temp, hum, alert


def secondary_code():
    """
    sensor = dht.DHT11(machine.Pin(22))

    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            print("Temperature: {}°C  Humidity: {}%".format(temp, hum))
        except OSError as e:
            print("Failed to read sensor:", e)
        
        utime.sleep(2)"""
    pass

while True:
    timestamp = utime.localtime()
    time_str = f"{timestamp[3]:02d}:{timestamp[4]:02d}:{timestamp[5]:02d}"
    # because the timestamp is given as a tuple and to turn the value in 2 dgits do :02 

    temp, hum, alert = read_dht11()
    print(f"{GREEN}[{time_str}] Temp: {temp:.1f}°C  Hum: {hum:.1f}% {alert}{RESET}")
    # reset to reset the color code

    utime.sleep(2) 
