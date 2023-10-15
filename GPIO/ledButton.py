#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""

import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling GPIO pins
import time
import signal
import sys

BUTTON = 18  # GPIO pin for the button
LED = 4    # GPIO pin for the LED
mybreak = 0
should_blink = False

# Define a signal handler to handle Ctrl+C and clean up GPIO
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

# Callback function for button press event
def button_press_callback(channel):
    global should_blink
    should_blink = not should_blink
    global mybreak
    mybreak = mybreak + 1

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set up the button as an input with a pull-up resistor
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up the LED as an output
GPIO.setup(LED, GPIO.OUT)

# Add an event detection for the button
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=button_press_callback, bouncetime=200)

# Register the signal handler to handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

while True:
    if mybreak >= 10:
        break

    if should_blink:
        GPIO.output(LED, GPIO.HIGH)  # Turn on the LED

    time.sleep(0.5)  # Sleep for 0.5 seconds

    if should_blink:
        GPIO.output(LED, GPIO.LOW)  # Turn off the LED

    time.sleep(0.5)  # Sleep for 0.5 seconds

# Clean up GPIO before exiting
GPIO.cleanup()
