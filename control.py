from pynput.mouse import Controller,Button


def controlMouse():
    mouse =  Controller()
    print("Moving")
    mouse.press(Button.right)    

controlMouse()
