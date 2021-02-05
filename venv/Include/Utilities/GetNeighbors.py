def get_neighbors(state_matrix, x, y):
    """
    For a given cell, computes the neighbors, check if they are valid and returns a list.
    :param state_matrix: Matrix containing the state of the game
    :param x: x coordinate of cell of interest
    :param y: y coordinante of cell of interest
    :return: List of valid neighbor cells
    """

    # initialize list of neighbors
    neighbors = []

    # Upper left neighbor, check if in the matrix
    if x - 1 >= 0 and y - 1 >= 0:
        # Check if the neighbor cell is playable
        if state_matrix[int(x) - 1, int(y) - 1] != -1:
            # Append the cell the the neighbor list
            neighbors.append([x - 1, y - 1])

    # Upper right neighbor, check if in the matrix
    if x + 1 < state_matrix.shape[0] and y - 1 >= 0:
        # Check if the neighbor cell is playable
        if state_matrix[x + 1, y - 1] != -1:
            # Append the cell the the neighbor list
            neighbors.append([x + 1, y - 1])

    # Lower right neighbor, check if in the matrix
    if x + 1 < state_matrix.shape[0] and y + 1 < state_matrix.shape[1]:
        # Check if the neighbor cell is playable
        if state_matrix[x + 1, y + 1] != -1:
            # Append the cell the the neighbor list
            neighbors.append([x + 1, y + 1])

    # Lower left neighbor, check if in the matrix
    if x - 1 >= 0 and y + 1 < state_matrix.shape[1]:
        # Check if the neighbor cell is playable
        if state_matrix[x - 1, y + 1] != -1:
            # Append the cell the the neighbor list
            neighbors.append([x - 1, y + 1])

    return neighbors