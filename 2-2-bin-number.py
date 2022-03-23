import RPi.GPIO as GPIO
import time
from  random import randint

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

number = []
for i in range(8):
    number.append(randint(0,2))

GPIO.output(dac, number)

time.sleep(10)

GPIO.output(dac, 0)

GPIO.cleanup()