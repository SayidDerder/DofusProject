import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.mouse import Button
from pynput.keyboard import Key
import time
import numpy as np
from Functions.VerifyCombat import VerifyCombat
from Functions.Combat import Combat
from Utilities.LoadMap import LoadMap
from Map import Map

mouse    = ms.Controller()
keyboard = kb.Controller()

if __name__ == "__main__":

    #Create a map object with parameters from file
    map = LoadMap("ForetAbraknyde")
    
    time.sleep(2)
    i = 15

    while (True):

        # Verify if in combat
        if VerifyCombat(mouse):
            Combat(mouse)
            
        # Loop for i going from 0 to 24
        i = i % 25
        
        # get mouse position
        pos = mouse.position
        
        # Set mouse position to the ressource postion
        mouse.position = map.ressource_positions[i]
        
        # Collect ressource
        mouse.click(Button.left, 1)
        
        # Set back mouse position to initial value
        mouse.position = pos
        
        # Wait until end of collect
        time.sleep(1)
        
        # increment counter
        i = i + 1
