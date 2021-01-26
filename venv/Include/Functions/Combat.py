import time
import numpy as np
import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.mouse import Button
from pynput.keyboard import Key

def Combat(mouse):
    # Coordinates of start cell for battles
    cell_pos = (1222, 642)

    # Coordinates of ready button
    ready_pos = (1854, 1313)

    # Coordinates of ready button
    spell_pos = (1655, 1282)

    # Coordinates of ready button
    close_pos = (1225, 827)

    # click on cell position
    mouse.position = cell_pos
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(1)

    # click on ready button
    mouse.position = ready_pos
    mouse.click(Button.left, 1)

    # Wait for adversary to play
    time.sleep(5)

    # click on spell
    mouse.position = spell_pos
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(1)

    # Cast spell
    mouse.position = cell_pos
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(3)

    # Close after combat window
    mouse.position = close_pos
    mouse.click(Button.left, 1)
    return