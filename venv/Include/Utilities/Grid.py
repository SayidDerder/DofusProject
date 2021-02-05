import numpy as np

def get_grid():
    """
    Function that create a matrix the size of the game containing the coordinates of each cell
    :return: 2*nb_x x 2*nn_y sized matrix with 0 for non valid cells and [coord1, coord2] for valid cells
    """

    # initialiue constants

    # Width of the game
    nb_x = 14

    # height of the game
    nb_y = 20

    # x and y coordinates difference
    delta_x = 120
    delta_y = 60

    # x and y offsets
    x_offset = 470
    y_offset = 45

    grid = np.zeros((2 * nb_x, 2 * nb_y, 2))

    for x in range(nb_x):
        for y in range(nb_y):
            grid[2 * x, 2 * y] = [delta_x * x + x_offset, delta_y * y + y_offset]

    for x in range(nb_x):
        for y in range(nb_y):
            grid[2 * x + 1, 2 * y + 1] = [delta_x * x + x_offset + delta_x / 2, delta_y * y + y_offset + delta_y / 2]

    return grid