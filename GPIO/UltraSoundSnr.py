#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""
import RPi.GPIO as GPIO
import time

class UltraSoundSnr:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def measure(self):
        try:
            GPIO.output(self.trigger_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trigger_pin, False)

            startTime = time.time()
            stopTime = time.time()
            while GPIO.input(self.echo_pin) == 0:
                startTime = time.time()
            while GPIO.input(self.echo_pin) == 1:
                stopTime = time.time()

            distance = (stopTime - startTime) * 34300 / 2  # Speed of sound = 343 meters per second
            return distance

        except KeyboardInterrupt:
            GPIO.cleanup()
