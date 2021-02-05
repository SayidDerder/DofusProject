from PIL import Image, ImageGrab
import time
import numpy as np
from Functions.Combat import Combat
from Functions.CombatCra import CombatCra

def VerifyCombat(mouse, map):
    
    # Coordinate of cell to check if in combat
    check_pos = map.check_pos
    print(check_pos)

    time.sleep(1)
    # Get screenshot
    screen = ImageGrab.grab(bbox=None)
    time.sleep(1)

    # Convert to array
    screen = np.asarray(screen)

    # Check if in combat by checking red array of image
    # Case not in combat
    print(screen[int(check_pos[1]),int(check_pos[0]),0])
    if screen[int(check_pos[1]),int(check_pos[0]),0] < 200:
        return False

    # Case in combat
    else:
        return True