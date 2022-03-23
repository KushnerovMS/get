import RPi.GPIO as GPIO
import time


def decimal2binary (value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


try:
    T = float(input ("Введите период в секундах:"))

    while True:
        for i in range (0, 255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T / 510)
        for i in range (254, 1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T / 510)

except KeyboardInterrupt:
    print ("Вы завершили процесс.")
except ValueError:
    print ("Вы ввели не число.")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()