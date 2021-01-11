from gpiozero import Motor, Button
from signal import pause

motor = Motor(24,25)
photoDiode = Button(20, bounce_time=0.25, pull_up=None, active_state=False)

onButton = Button(22)

spins = 0
motor.stop()

def motorOn():
    global spins
    spins = 0
    print("motorOn called")
    motor.forward()
    
def lightSense():
    global spins
    spins = spins + 1
    print("Light sensor triggered: ", spins)
    if spins > 9:
        motor.stop()
        print("motor off")
        
onButton.when_pressed = motorOn
photoDiode.when_pressed = lightSense


#Prevent the script from exiting
print("\n\n=========================\nPress Ctrl-C ('Ctrl' and 'c' together) when ready to exit ...\n");
pause()