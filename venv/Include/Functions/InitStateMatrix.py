from PIL import Image, ImageGrab
import time
import numpy as np


def init_state_matrix(grid):
    """

    :param grid: nb_x*nb_y sized matrix containing the coordiantes of every cell
    :param map_params: Colors of the map.
    :return: nb_x*nb_y sized matrix with 0 for playable cells, 1 for ally and 2 for enemy. -1 is not valid cell.
    """


    # Initialize constants
    nb_x = 14
    nb_y = 20

    # TODO : Change Map loader to integrate map colors and stuff
    # Base Sufokia:
    map_colors = [203, 193]
    GREEN = [122, 116]
    RED = 221
    ENEMY_START_RED = [143, 136]
    ENEMY_START_BLUE = [115, 122]


    # Take a screenshot and process the image into red and blue arrays
    time.sleep(1)
    screen = ImageGrab.grab(bbox=None)
    time.sleep(1)
    red = np.asarray(screen)[:, :, 0]
    blue = np.asarray(screen)[:, :, 2]

    start_cells = []

    # Loop over all grid cells
    for i in range(2 * nb_x):
        for j in range(2 * nb_y):
            pos = grid[i, j]

            # If a valid cell
            if pos is not [0, 0]:

                # if the right of the cell is red (Ally placement)
                if red[int(pos[1]), int(pos[0]) + 40] == RED:

                    # Add cell to starting cell list
                    start_cells.append(list(pos))

                    # If the center of red cell is not red --> Ally is on this cell
                    if red[int(pos[1]) - 20, int(pos[0])] != red[int(pos[1]), int(pos[0]) + 40]:
                        pos_character = pos
                        index_character = np.array([i, j])

                # if the left of the cell is red (Ally placement). Only check if right wasn't red, case of an obstacle
                elif red[int(pos[1]), int(pos[0]) - 40] == RED:

                    # Add cell to starting cell list
                    start_cells.append(list(pos))

                    # If the center of red cell is not red --> Ally is on this cell
                    if red[int(pos[1]) - 20, int(pos[0])] != red[int(pos[1]), int(pos[0]) - 40] and list(
                            pos) not in start_cells:
                        pos_character = pos
                        index_character = np.array([i, j])

                # if the right of the cell is blue (Enemy placement)
                elif red[int(pos[1]), int(pos[0]) + 40] in ENEMY_START_RED and blue[
                    int(pos[1]), int(pos[0]) + 40] in ENEMY_START_BLUE:

                    # Add cell to starting cell list
                    start_cells.append(list(pos))

                    # If the center of blue cell is not blue --> Enemy is on this cell
                    if red[int(pos[1]) - 20, int(pos[0])] != red[int(pos[1]), int(pos[0]) + 40]:
                        pos_enemy = pos
                        index_enemy = np.array([i, j])

                # if the right of the cell is blue (Enemy placement). Only check if right wasn't blue, case of an obstacle
                elif red[int(pos[1]), int(pos[0]) - 40] in ENEMY_START_RED and blue[
                    int(pos[1]), int(pos[0]) - 40] in ENEMY_START_BLUE and list(pos) not in start_cells:

                    # Add cell to starting cell list
                    start_cells.append(list(pos))

                    # If the center of blue cell is not blue --> Enemy is on this cell
                    if red[int(pos[1]) - 20, int(pos[0])] != red[int(pos[1]), int(pos[0]) - 40]:
                        pos_enemy = pos
                        index_enemy = np.array([i, j])


    # Initialize state matrix with -1's )
    state_matrix = np.ones([2 * nb_x, 2 * nb_y]) * (-1)

    # Loop over all cells
    for i in range(2 * nb_x):
        for j in range(2 * nb_y):
            pos = grid[i, j]

            # if a valid cell
            if pos.any():

                # if its a playable cell
                if red[int(pos[1]), int(pos[0]) - 40] in map_colors or list(pos) in start_cells or red[
                    int(pos[1]) - 10, int(pos[0])] in map_colors:

                    # Value 0 for a empty but playable cell
                    state_matrix[i, j] = 0

    # 1 is for ally cell, 2 for ennemy cell
    state_matrix[index_enemy[0], index_enemy[1]] = 2
    state_matrix[index_character[0], index_character[1]] = 1

    return state_matrix