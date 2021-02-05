import time
import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.mouse import Button
from pynput.keyboard import Key

def cast_spell(enemy_position):
    """
    cast a specific spell on the enemy
    :param enemy_position: [x,y] coordinates of the ennemy
    :return:
    """

    # inititize mouse and keyborad
    mouse = ms.Controller()
    keyboard = kb.Controller()

    # Coordinates of spell to cast
    SPELL = (1200, 1280)

    # save current position of the mouse
    p = mouse.position

    # click on the spell
    mouse.position = SPELL
    mouse.click(Button.left, 1)
    time.sleep(0.5)

    # Click on the ennemy position
    mouse.position = enemy_position
    mouse.click(Button.left, 1)

    # restore previously saved position of the mouse
    mouse.position = p
    return