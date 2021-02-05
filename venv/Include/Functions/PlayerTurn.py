from PIL import Image, ImageGrab
import time
import numpy as np

def player_turn():
    """
    Checks if its the players turn to play
    :return: True if it is his turn, False otherwize
    """

    # Coordinates of the place to check if players turn
    CHECK = (1900, 1300)

    # Get screenshot
    time.sleep(1)
    screen = ImageGrab.grab(bbox=None)
    time.sleep(1)

    # Convert to red array
    red = np.asarray(screen)[:, :, 0]

    # if pixel value at check position is right, return True, else return False
    if red[CHECK[1], CHECK[0]] == 207 or red[CHECK[1], CHECK[0]] == 236:
        return True
    else:
        return False