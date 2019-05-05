import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buttonPin = 24

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

raw_input("Press Enter when ready\n>")

try:
	GPIO.wait_for_edge(buttonPin, GPIO.FALLING)
	print("BUTTON PRESSED")

except keyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()

