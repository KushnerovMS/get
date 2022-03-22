import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

while True:
    GPIO.output(5, not GPIO.input(6))
