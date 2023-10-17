#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""
import RPi.GPIO as GPIO
import time

class ServoClass:
    def __init__(self, servo_pin, pwm_freq=50):
        # Initialize the servo motor with a GPIO pin and PWM frequency
        self.servo_pin = servo_pin
        self.pwm_freq = pwm_freq
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.servo_pin, self.pwm_freq)

    def setAngle(self, angle):
        # Set the servo motor's position based on the desired angle
        try:
            # Calculate PWM duty cycle for the given angle
            duty_cycle = int((angle -1)*(13-2)/(180-1)+2)
            self.servo.start(0)
            self.servo.ChangeDutyCycle(duty_cycle)
            time.sleep(1)  # Wait for 1 second
        except KeyboardInterrupt:
            pass
    def cleanup(self):
        # Clean up and release the GPIO resources
        self.servo.stop()
        GPIO.cleanup()

