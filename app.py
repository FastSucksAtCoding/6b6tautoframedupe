import mouse, keyboard
import time

toggled = False

while True:
    if keyboard.is_pressed("ctrl + 0"):
        if toggled != True:
            toggled = True
        else:
            toggled = False
    if toggled:
        toggled2 = True
        while toggled2 == True:
            if keyboard.is_pressed("ctrl + 0"):
                if toggled2 != True:
                    toggled2 = True
                else:
                    toggled = False
                    toggled2 = False
            mouse.hold(mouse.RIGHT)
            time.sleep(3)
            mouse.release(mouse.RIGHT)
            mouse.click(mouse.LEFT)
            toggled2 = False
            time.sleep(0.5)
            toggled2 = True
