import RPi.GPIO as GPIO


def decimal2binary (value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        try:
            val = input ("Введите число: ")
            if (val == "q"):
                break
            if (float(val) % 1 != 0):
                print ("Вы ввели дробное число, попробуйте еще раз")
                continue

            val = int(val)

            if (val < 0):
                print ("Число должно быть положительным")
                continue
            if (val >= 256):
                print ("Вы перешли пороговое значение в 255")
                continue

            print ("Расчитываемое значения напряжения: {:.2f}".format(3.3 / (2 ** 8) * val))
            GPIO.output(dac, decimal2binary(val))

        except ValueError:
            print ("Вы ввели не число, попробуйте еще раз")
            continue

except KeyboardInterrupt:
    print ("\nВы завершили процесс.")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()