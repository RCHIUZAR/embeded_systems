#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""
import RPi.GPIO as GPIO
from UltraSoundSnr import UltraSoundSnr  # Import the UltraSoundSnr class from your module
import time
try:
    trigger_pin = 24  # Replace with the actual GPIO pin number for the trigger
    echo_pin = 23    # Replace with the actual GPIO pin number for the echo

    ultrasonic_sensor = UltraSoundSnr(trigger_pin, echo_pin)

    while True:
        distance = ultrasonic_sensor.measure()
        print(f"Distance: {distance:.1f} cm")
        time.sleep(1)  # Delay between measurements

except KeyboardInterrupt:
    print("Measurement stopped by the user")
finally:
    GPIO.cleanup()
