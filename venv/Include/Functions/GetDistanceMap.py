import numpy as np
from Utilities.Dist import dist
from Utilities.GetNeighbors import get_neighbors

def get_distance_map(state_matrix):
    """
    Compute the distances of all cells from ally position to ennemy positons taking obstacles into account
    :param state_matrix: State of the game
    :return: 2*nb_x x 2*nb_y sized array containing the distances to the ennemy position
    """

    # Search for enemy position
    for i in range(state_matrix.shape[0]):
        for j in range(state_matrix.shape[1]):
            # is state matrix = 2 --> Enemy
            if state_matrix[i, j] == 2:
                enemy_position = [i, j]

    # Q = List of cells to calculate position
    Q = [list(enemy_position)]

    # List of already visited cells
    V = []

    # Initialize state matrix with -1's
    distance_matrix = np.ones(state_matrix.shape) * (-1)

    # Put in 0 at enemy position
    distance_matrix[enemy_position[0], enemy_position[1]] = 0

    # k is to make sure loop ends
    k = 0

    # While Q is not empty
    while Q and k < 1000:

        # Node n = to the first element of the list
        n = Q[0]

        # Get neighbors of current cell
        neighbors = get_neighbors(state_matrix, n[0], n[1])

        # for each neighbor, if we havent already checked it and if its not already in the list, add to the list
        for neighbor in neighbors:
            if not neighbor in V and not neighbor in Q:
                Q.append(list(neighbor))

        # if the current is the ally cell
        if state_matrix[n[0], n[1]] == 1:
            # add coresponding distance and end
            distance_matrix[n[0], n[1]] = dist(distance_matrix, state_matrix, neighbors)
            break

        # if cell is not the enemy cell, add corresponding distance to the distance map
        if n != list(enemy_position):
            distance_matrix[n[0], n[1]] = dist(distance_matrix, state_matrix, neighbors)

        # add cell to the list of visited cells
        V.append(n)

        # remove cell from the list of cells to visit
        del Q[0]

        k += 1
    return distance_matrix