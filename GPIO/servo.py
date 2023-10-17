#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""
import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling GPIO pins
import time
import sys

def angleToDuty(angle):
    # Convert an angle to PWM duty cycle
    return int((angle - 1) * (13 - 2) / (180 - 1) + 2)

# Read the desired angle from the command-line argument
angle2 = int(sys.argv[1])

# Set the GPIO pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the servo
servoPin = 17

# Define the PWM frequency (50 Hz)
pwmFreq = 50

# Configure the servo pin as an output
GPIO.setup(servoPin, GPIO.OUT)

# Create a PWM (Pulse Width Modulation) object for the servo
servo = GPIO.PWM(servoPin, pwmFreq)

# Start the PWM with a duty cycle corresponding to the desired angle
servo.start(0)
servo.ChangeDutyCycle(angleToDuty(angle2))

# Wait for 1 second
time.sleep(1)

# Stop the PWM
servo.stop()

# Clean up and release the GPIO resources
GPIO.cleanup()
