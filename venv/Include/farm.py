import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.mouse import Button
from pynput.keyboard import Key
import time
import numpy as np

from Functions.CheckIfInCombat import check_if_in_combat
from Functions.AutoBattle import AutoBattle

from Utilities.LoadMap import LoadMap
from Map import Map

mouse    = ms.Controller()
keyboard = kb.Controller()

if __name__ == "__main__":

    #Create a map object with parameters from file
    map = LoadMap("PiscineSufokia2")
    
    time.sleep(2)
    i = 0

    while (True):
            
        # Loop for i going from 0 to 24
        i = i % len(map.ressource_positions)

        # Check for combat
        if check_if_in_combat():
            AutoBattle()
        
        # get mouse position
        pos = mouse.position
        
        # Set mouse position to the ressource postion
        mouse.position = map.ressource_positions[i]
        
        # Collect ressource
        mouse.click(Button.left, 1)
        
        # Set back mouse position to initial value
        mouse.position = pos
        
        # Wait until end of collect
        time.sleep(3)
        
        # increment counter
        i = i + 1
