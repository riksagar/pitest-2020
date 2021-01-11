from gpiozero import RGBLED
from colorzero import Color
from time import sleep

led = RGBLED(18, 19, 20)


redVal = 0.5;
greenVal = 0.5;
while True:
    sleep(0.1)
    redVal += 0.2/5
    greenVal += 0.4/5
    if (redVal > 1):
        redVal = 0.1;
    if (greenVal > 1):
        greenVal = 0.1
    led.value = (redVal, greenVal, 0)
    

    