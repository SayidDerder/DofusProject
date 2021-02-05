def get_positions(state_matrix):
    """
    Check the state matrix to find the positions of the players
    :param state_matrix: Matrix describing the current state of the game
    :return: [x_p, y_p], [x_e, y_e] positions of the player and of the enemy
    """

    # Loop over all elements of the matrix
    for i in range(state_matrix.shape[0]):
        for j in range(state_matrix.shape[1]):
            # 1 --> player position
            if state_matrix[i, j] == 1:
                player_position = [i, j]
            # 2 --> Enemy position
            elif state_matrix[i, j] == 2:
                enemy_position = [i, j]

    return player_position, enemy_position