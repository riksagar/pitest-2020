from gpiozero import Servo
from time import sleep

servo = Servo(6,min_pulse_width = 1.3/1000,max_pulse_width = 1.7/1000)

for i in range(-10,10,1):
    servo.value = i/10
    sleep(0.5)