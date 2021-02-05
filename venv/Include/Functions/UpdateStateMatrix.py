from PIL import Image, ImageGrab
import time
import numpy as np

def update_state_matrix(old_matrix, grid, player):
    """

    :param old_matrix: Previous State matrix
    :param grid: Matrix containing coordinates of the world
    :param player: Boolean variable, true if player turn, false otherwise
    :return: 2*nb_x x 2*nb_y sized matrix containing the new state of the game

    """

    # init constants
    nb_x = 14
    nb_y = 20

    # Base Sufokia: TOCHANGE
    map_colors = [203, 193]
    GREEN = [122, 116]
    RED = 221
    BLUE = [143, 136]


    # Get screenshot
    time.sleep(1)
    screen = ImageGrab.grab(bbox=None)
    time.sleep(1)

    # Convert to array
    red = np.asarray(screen)[:, :, 0]

    # init new state matrix with -1's
    new_matrix = np.ones(old_matrix.shape) * (-1)

    # Allows to update the matrix according to which player has played
    if player:
        number = 1
    else:
        number = 2

    # loop over all cells
    for i in range(2 * nb_x):
        for j in range(2 * nb_y):
            pos = grid[i, j]
            if pos.any():

                # If cell is empty --> 0
                if red[int(pos[1]) - 10, int(pos[0])] in map_colors or red[int(pos[1]) - 10, int(pos[0])] in GREEN:
                    new_matrix[i, j] = 0

                # If cell not empty, but was empty before --> number
                elif new_matrix[i, j] != old_matrix[i, j] and old_matrix[i, j] == 0:
                    new_matrix[i, j] = number

                # Case player hasn't moved --> number
                elif new_matrix[i, j] == -1 and old_matrix[i, j] == number:
                    new_matrix[i, j] = number

                # if cell wasn't empty, and still isn't. Case other player --> old_matrix[i,j]
                elif new_matrix[i, j] != old_matrix[i, j] and old_matrix[i, j] != 0 and old_matrix[i, j] != -1 and \
                        old_matrix[i, j] != number:
                    new_matrix[i, j] = old_matrix[i, j]

    return new_matrix