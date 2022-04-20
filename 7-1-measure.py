import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

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
    valList = []
    beginTime = time.time()

    curVal = 0

    GPIO.output(troyka, 1)
    while (curVal < 0.97 * 225):
        curVal = adc()
        valList.append(curVal)
        GPIO.output(leds, decimal2binary(curVal))
        print (curVal)

    GPIO.output(troyka, 0)
    while (curVal > 0.02 * 225):
        curVal = adc()
        valList.append(curVal)
        GPIO.output(leds, decimal2binary(curVal))
        print (curVal)

    endTime = time.time()
    deltaTime = endTime - beginTime

    plt.title("Зависимость напряжения от измерения")
    plt.plot (valList)

    plt.show()

    with open("./data.txt", "w") as file:
        file.write("\n".join([str(item) for item in valList]))

    with open("./settings.txt", "w") as file:
        file.write("%f\n" % (len(valList) / deltaTime))
        file.write("%f\n" % (3.3 / 256))

    print("Продолжительность эксперимента: %fc" % deltaTime)
    print("Период одного эксперимента: %fc" % (deltaTime / len (valList)))
    print("Средняя частота дискретизации: %fГц" % (len (valList) / deltaTime))
    print("Шаг квантования АЦП: %fВ" % (3.3 / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()