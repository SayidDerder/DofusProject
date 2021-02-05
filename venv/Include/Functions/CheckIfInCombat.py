from PIL import Image, ImageGrab
import time
import numpy as np


def check_if_in_combat():

    # Coordinate of place to check if in combat
    CHECK = (1938, 1370)

    # Get screenshot
    time.sleep(0.5)
    screen = ImageGrab.grab(bbox=None)
    time.sleep(0.5)

    #Convert to red array
    red = np.asarray(screen)[:, :, 0]

    # Check in a 5 by 5 square if any of the pixels are right and return True if in combat, False if not
    for i in range(-2, 3):
        for j in range(-2, 3):
            if red[CHECK[1] + i, CHECK[0] + j] == 197:
                return True

    return False