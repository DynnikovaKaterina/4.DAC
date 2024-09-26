import RPi.GPIO as gp
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        print("Введите целое число от 0 до 255:")
        value = input()
        if value == "q":
            break
        print("Введите период:")
        T = int(input())
        value = int(value)
        for decimal in range(value, 256):
            binary = decimal2binary(decimal)
            for i in range(8):
                gp.output(dac[i], binary[i])
            time.sleep(T / ((255 - value) * 2) )
        for decimal in range(255, value - 1, -1):
            binary = decimal2binary(decimal)
            for i in range(8):
                gp.output(dac[i], binary[i])
            time.sleep(T / ((255 - value) * 2) )

finally:
    gp.output(dac, 0)
    gp.cleanup()