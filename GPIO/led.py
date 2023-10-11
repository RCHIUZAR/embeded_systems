#!/usr/bin/python3
import Rpi.GPIO as GPIO
import time

LedPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin,GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)
time.slep(5)
GPIO.output(LedPin, GPIO.LOW)
GPIO.cleanup()


