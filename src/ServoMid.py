from gpiozero import Servo

servo = Servo(6,min_pulse_width = 1.3/1000,max_pulse_width = 1.7/1000)

servo.mid()