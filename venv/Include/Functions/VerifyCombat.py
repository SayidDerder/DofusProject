from PIL import Image, ImageGrab
import time
import numpy as np
from Functions.Combat import Combat

def VerifyCombat(mouse):
    
    # Coordinate of cell to check if in combat
    check_pos = (1461, 764)

    time.sleep(1)
    # Get screenshot
    screen = ImageGrab.grab(bbox=None)
    time.sleep(1)

    # Convert to array
    screen = np.asarray(screen)

    # Check if in combat by checking red array of image
    # Case not in combat
    if screen[check_pos[1], check_pos[0], 0] < 200:
        return False

    # Case in combat
    else:
        return True