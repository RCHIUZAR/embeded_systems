#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""

import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling GPIO pins
import time

triggerGpioPin = 24
echoGpioPin = 23

GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering mode to BCM
GPIO.setup(triggerGpioPin, GPIO.OUT)  # Set the trigger pin as an output
GPIO.setup(echoGpioPin, GPIO.IN)  # Set the echo pin as an input

def measure():
    # Send a trigger pulse
    GPIO.output(triggerGpioPin, True)
    time.sleep(0.00001)
    GPIO.output(triggerGpioPin, False)

    startTime = time.time()
    stopTime = time.time()
    while GPIO.input(echoGpioPin) == 0:
        startTime = time.time()
    while GPIO.input(echoGpioPin) == 1:
        stopTime = time.time()

    # Calculate the distance based on the time difference
    distance = (stopTime - startTime) * 34300 / 2  # Speed of sound = 343 meters per second
    return distance

if __name__ == '__main__':
    try:
        while True:
            # Continuously measure and print the distance
            print("distance = %.1f" % measure())
            time.sleep(0.5)  # Wait for 0.5 seconds before the next measurement

    except KeyboardInterrupt:
        print("Measurement stopped by the user")
        GPIO.cleanup()  # Clean up and release the GPIO resources when the program is terminated

