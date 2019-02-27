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

# read data using pin 18
instance = dht11.DHT11(pin=18)

while True:
    result = instance.read()
    if result.is_valid():
        print('{},Temp:{},Humid:{}'.format(datetime.datetime.now(), result.temperature, result.humidity))
        ambi = ambient.Ambient(os.environ["AMBIENT_ID"], os.environ["AMBIENT_WTOKEN"])
        r = ambi.send({"d1": result.temperature, "d2": result.humidity})
