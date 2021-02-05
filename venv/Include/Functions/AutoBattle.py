import time
import pynput.mouse    as ms
import pynput.keyboard as kb
from pynput.mouse import Button
from pynput.keyboard import Key

from Utilities.Grid import get_grid
from Utilities.GetPositions import get_positions
from Functions.InitStateMatrix import init_state_matrix
from Functions.CheckIfInCombat import check_if_in_combat
from Functions.PlayerTurn import player_turn
from Functions.UpdateStateMatrix import update_state_matrix
from Functions.GetDistanceMap import get_distance_map
from Functions.GetMovePosition import get_move_position
from Functions.CastSpell import cast_spell

mouse    = ms.Controller()
keyboard = kb.Controller()

def AutoBattle():
    """
    Script that is able to play a simple 1v1 combat
    """

    # Ready button position
    READY = (1900, 1300)

    # Check if player turn to play position
    CHECK = (1938, 1370)

    # End of combat screen position
    END = (1219, 836)

    # Load grid
    grid = get_grid()

    # Initialize state matrix
    state_matrix = init_state_matrix(grid)

    # Save mouse position
    p = mouse.position

    # Click ready button
    mouse.position = READY
    mouse.click(Button.left, 1)

    # restore mouse position
    mouse.position = p

    # While in combat
    while check_if_in_combat():

        # If player turn to play
        if player_turn():

            # Update state matrix knowing ennemy has just played
            state_matrix = update_state_matrix(state_matrix, grid, player=False)

            # Calculate distance map
            distance_map = get_distance_map(state_matrix)

            # Calculate if and where to move
            next_move, move = get_move_position(state_matrix, distance_map)

            # If player has to move
            if move:
                # Save current mouse position
                p = mouse.position

                # Click on move location
                mouse.position = grid[next_move[0], next_move[1]]
                time.sleep(0.05)
                mouse.click(Button.left, 1)
                time.sleep(1.5)

                # Restore mouse position
                mouse.position = p

                # Update the state matrix knowing the player has just played
                state_matrix = update_state_matrix(state_matrix, grid, player=True)

                # Update distance map
                distance_map = get_distance_map(state_matrix)

            # get enemy and player positions
            player_position, enemy_position = get_positions(state_matrix)

            # If the distance between the player and the enemy is less than 14 (range of spell), cast the spell
            if distance_map[player_position[0], player_position[1]] < 14:
                cast_spell(grid[enemy_position[0], enemy_position[1]])

            # End the turn
            p = mouse.position
            mouse.position = READY
            mouse.click(Button.left, 1)
            mouse.position = p

    # When batlle has ended, close pop up window
    mouse.position = END
    mouse.click(Button.left, 1)