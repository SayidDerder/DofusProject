import numpy as np

def dist(dm, sm, neighbors):
    """
    computes the distance of a given cell to the enemy position
    :param dm: Distance map
    :param sm: State matrix
    :param neighbors: Neighbors of the given cell
    :return: distance to enemy cell
    """

    # Initialize list of possible distances
    distances = []

    # loop over all neighbors of the cell
    for neighbor in neighbors:
        # If the neighbor is valid
        if dm[neighbor[0], neighbor[1]] != -1:
            # add neighbor distance + 1 to possible distances
            distances.append(dm[neighbor[0], neighbor[1]] + 1)

    # return minimal distance
    return np.min(distances)