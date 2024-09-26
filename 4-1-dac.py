import RPi.GPIO as gp
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        print("Введите целое число от 0 до 255:")
        decimal = input()
        if decimal == "q":
            break
        elif not decimal.isdigit() or int(decimal) < 0 or int(decimal) > 255:
            print("Некорректный ввод")
        else:
            binary = decimal2binary(int(decimal))
            for i in range(8):
                gp.output(dac[i], binary[i])
            U_out = 3.3 * int(decimal) / 256 
            print("Напряжение на выходе ЦАП в Вольтах:", U_out)
finally:
    gp.output(dac, 0)
    gp.cleanup()
