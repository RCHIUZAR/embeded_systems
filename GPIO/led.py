#!/usr/bin/python3
import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling GPIO pins
import time

LedPin = 4  # Define the GPIO pin (BCM mode) to which the LED is connected

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set the LedPin as an output pin
GPIO.setup(LedPin, GPIO.OUT)

# Turn on the LED by setting the output to HIGH
GPIO.output(LedPin, GPIO.HIGH)

# Wait for 5 seconds
time.sleep(5)  # Note the corrected function name "time.sleep" instead of "time.slep"

# Turn off the LED by setting the output to LOW
GPIO.output(LedPin, GPIO.LOW)

# Clean up and release the GPIO resources
GPIO.cleanup()


