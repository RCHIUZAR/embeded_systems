#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""

from ledClass import LED  # Import the LED class from your module

# Initialize an instance of the LED class with GPIO pin 4
led = LED(4)

try:
    # Turn on the LED
    print("Turning the LED on...")
    led.ledOn()
    input("Press Enter to continue...")

    # Turn off the LED
    print("Turning the LED off...")
    led.ledOff()
    input("Press Enter to continue...")

    # Blink the LED for 10 seconds with a 1-second interval
    print("Blinking the LED for 10 seconds with a 1-second interval...")
    led.ledBlink(10, 1)
except KeyboardInterrupt:
    print("Execution interrupted by user.")
finally:
    # Clean up GPIO resources
    led.cleanup()
