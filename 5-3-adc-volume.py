import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17



GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary (value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def binary2decimal (bin):
    dec = 0
    for i in range (8):
        dec += bin[i] << (7 - i)

    return dec

def adc ():
    val = decimal2binary(0)

    for i in range (8):
        val[i] = 1
        GPIO.output(dac, val)
        time.sleep (0.001)
        if (GPIO.input(comp) == 0):
            val[i] = 0

    return binary2decimal(val)
            
try:
    while True:
        #GPIO.output(dac, decimal2binary(1))
        #print (GPIO.input(comp))
        value = adc()
        GPIO.output(leds, decimal2binary((1 << int((value / 28))) - 1))
        print (decimal2binary(value))
        print ("%d %.2fV" % (value, 3.3 / 256 * value))

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()