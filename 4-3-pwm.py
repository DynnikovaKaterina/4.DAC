import RPi.GPIO as gp
gp.setmode(gp.BCM)
gp.setup(9, gp.OUT)
pwm = gp.PWM(9, 100)#объект управления ШИМом
pwm.start(0)

try:
    while True:
        value = int(input())
        pwm.ChangeDutyCycle(value) #где value - float от 0.0 до 100.0
finally:
    gp.output(9, 0)
    gp.cleanup()