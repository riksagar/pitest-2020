from gpiozero import Button

btn = Button(20, bounce_time=0.25, pull_up=None, active_state=True)
count = 0

def onPressed():
    global count
    count += 1
    print("pressed", count)
    
btn.when_pressed = onPressed
    