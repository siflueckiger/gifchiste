#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import atexit

#Variables to change as needed
btn_pin = 24 # pin for the button
debounce = 0.5 # how long to debounce the button. Add more time if the button triggers too many times.

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def cleanup():
  print('Goodbye.')
  GPIO.cleanup()
atexit.register(cleanup)

print('Push Button')
print('Press Ctrl+C to exit')

while True:
	GPIO.wait_for_edge(btn_pin, GPIO.RISING)
	sleep(debounce)
	print("Button pressed")
