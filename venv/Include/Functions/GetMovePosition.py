from Utilities.GetNeighbors import get_neighbors

def get_move_position(state_matrix, distance_map):
    """
    Function that calculates to which cell the player has to move
    :param state_matrix: Matrix describing the state of the game
    :param distance_map: Matrix describtion the distances of each cell to the ennemy position
    :return: position : [x,y] the cell to which the player has to move, True/False, if the player has to move or not.
    """

    # Loop over the state matrix to find the player position
    for i in range(state_matrix.shape[0]):
        for j in range(state_matrix.shape[1]):
            if state_matrix[i, j] == 1:
                character_position = [i, j]
                break

    position = character_position

    # if the ally is next to the ennemy, return its position and False --> no need to move
    if distance_map[position[0], position[1]] == 1:
        return position, False

    # Init distance to arbitrarily high value
    min_distance = 1000

    # Loop 6 times: number of movement points
    for i in range(5):
        # if the player can arrive next to the ennemy, stop and return position and True
        if distance_map[position[0], position[1]] == 1:
            break

        # Else, check each neighbor and move the the one closest to the ennemy
        neighbors = get_neighbors(state_matrix, position[0], position[1])
        for neighbor in neighbors:
            if distance_map[neighbor[0], neighbor[1]] != -1 and distance_map[neighbor[0], neighbor[1]] < min_distance:
                min_distance = distance_map[neighbor[0], neighbor[1]]
                position = neighbor
    return position, True