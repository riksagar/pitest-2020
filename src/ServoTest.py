from gpiozero import Servo
from time import sleep

servo = Servo(6,min_pulse_width = 1.3/1000,max_pulse_width = 1.7/1000)

while True:
    servo.min()
    print('min')
    sleep(1)
    servo.detach()
    print('detach')
    sleep(1)
    servo.max()
    print('max', servo.value)
    sleep(1)
    servo.mid()
    sleep(0.01)
    servo.detach()
    print('brake')
    sleep(1)