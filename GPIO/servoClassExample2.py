#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""
from servoClass import ServoClass  # Import the ServoClass from your module
import RPi.GPIO as GPIO
import sys
import time

servo_pin = 17  # Replace with the actual GPIO pin number for the servo
pwm_freq = 50   # PWM frequency (default is 50 Hz)

servo_motor = ServoClass(servo_pin, pwm_freq)
angle = int(sys.argv[1])
if 0 <= angle <= 180:
         servo_motor.setAngle(angle)
         time.sleep(5)
         servo_motor.setAngle(angle+20)
else:
         print("Invalid angle. Angle should be between 0 and 180 degrees.")

servo_motor.cleanup()
