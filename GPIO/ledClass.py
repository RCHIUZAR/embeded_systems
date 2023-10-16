#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""

import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, pin):
        # Initialize the LED using the given GPIO pin
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def ledBlink(self, duration, interval):
        # Blink the LED for the specified duration (in seconds) with the given interval (in seconds)
        try:
            while duration > 0:
                GPIO.output(self.pin, GPIO.HIGH)  # Turn the LED on
                time.sleep(interval)
                GPIO.output(self.pin, GPIO.LOW)   # Turn the LED off
                time.sleep(interval)
                duration -= interval
        except KeyboardInterrupt:
            pass
        finally:
            self.ledOff()  # Ensure the LED is turned off when done

    def ledOn(self):
        # Turn the LED on
        GPIO.output(self.pin, GPIO.HIGH)

    def ledOff(self):
        # Turn the LED off
        GPIO.output(self.pin, GPIO.LOW)

    def cleanup(self):
        # Clean up the GPIO resources
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        led = LED(4)  # Initialize the LED on GPIO pin 4
        led.ledOn()   # Turn the LED on
        time.sleep(3) # Keep the LED on for 3 seconds
        led.ledOff()  # Turn the LED off
        time.sleep(1) # Pause for 1 second
        led.ledBlink(5, 0.5)  # Blink the LED for 5 seconds with a 0.5-second interval
    finally:
        led.cleanup()  # Clean up GPIO resources when done
