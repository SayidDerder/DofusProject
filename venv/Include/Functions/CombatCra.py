import time
import numpy as np
import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.mouse import Button
from pynput.keyboard import Key

def CombatCra(mouse, map):
    # Coordinates of start cell for battles
    cell_pos = map.check_pos

    # Coordinates of ready button
    ready_pos = (1854, 1313)

    # Coordinates of 1st spell: Arrow
    spell_pos1 = (1655, 1282)

    # Coordinates of 2nd spell: portée
    spell_pos2 = (1140, 1339)

    # Coordinates of 3rd spell: 40 dammage
    spell_pos3 = (1313, 1342)

    # Coordinates of the ennemy
    ennemy_pos = (2240, 1119)

    # Coordinates of the close button
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
    mouse.position = spell_pos2
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(1)

    # Cast spell
    mouse.position = cell_pos
    mouse.click(Button.left, 1)

    # click on spell
    mouse.position = spell_pos3
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(1)

    # Cast spell
    mouse.position = cell_pos
    mouse.click(Button.left, 1)

    # click on spell
    mouse.position = spell_pos1
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(1)

    # Cast spell
    mouse.position = ennemy_pos
    mouse.click(Button.left, 1)

    # wait 1s
    time.sleep(3)

    # Close after combat window
    mouse.position = close_pos
    mouse.click(Button.left, 1)
    return