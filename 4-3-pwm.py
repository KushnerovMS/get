import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
g = GPIO.PWM(2, 100000)

g.start(0)

try:
    while True:
        try:
            val = input ("Введите заполненость в процентах: ")
            if (val == "q"):
                break

            val = float(val)

            if (val < 0):
                print ("Заполненность должна быть положительной")
                continue
            if (val > 100):
                print ("Вы перешли пороговое значение в 100%")
                continue

            g.stop()
            g.start(val)

        except ValueError:
            print ("Вы ввели не число, попробуйте еще раз")
            continue

except KeyboardInterrupt:
    print ("\nВы завершили процесс.")
finally:
    g.stop()
    GPIO.cleanup()