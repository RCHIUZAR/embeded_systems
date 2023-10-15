#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""

import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling GPIO pins
import time

LedPin = 4  # Define the GPIO pin (BCM mode) to which the LED is connected

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set the LedPin as an output pin
GPIO.setup(LedPin, GPIO.OUT)

for i in range(10): 
	# Turn on the LED by setting the output to HIGH
	GPIO.output(LedPin, GPIO.HIGH)

	# Wait for .5 seconds
	time.sleep(.5) 

	# Turn off the LED by setting the output to LOW
	GPIO.output(LedPin, GPIO.LOW)
	# Wait for .5 seconds
	time.sleep(.5)  


# Clean up and release the GPIO resources
GPIO.cleanup()
