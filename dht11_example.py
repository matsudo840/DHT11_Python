#!/usr/bin/python3
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import ambient
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    if result.is_valid():
        with open('dht11_example.log', 'a', encoding='utf-8') as f:
            f.write('{},Temp:{},Humid:{}\n'.format(datetime.datetime.now(), result.temperature, result.humidity))
        ambi = ambient.Ambient(os.environ["AMBIENT_ID"], os.environ["AMBIENT_WTOKEN"])
        r = ambi.send({"d1": result.temperature, "d2": result.humidity})
        break
    time.sleep(1)
