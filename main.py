a_board1 = []
for i in range(100):
    if i == 3:
        a_board1.append(13)
    elif i == 8:
        a_board1.append(30)
    elif i == 15:
        a_board1.append(5)
    elif i == 20:
        a_board1.append(41)
    elif i == 27:
        a_board1.append(83)
    elif i == 35:
        a_board1.append(43)
    elif i == 45:
        a_board1.append(25)
    else:
        a_board1.append(0)


def die():
    import random
    return random.randint(1, 6)


def player_movement(board, pos):
    steps = die()

    if pos + steps > len(board) - 1:
        return pos
    if pos + steps == len(board) - 1:
        return -1
    if board[pos + steps] != 0:
        return board[pos + steps]
    if board[pos + steps] == 0:
        return pos + steps


def player_control(player_dict):
    for j in range(len(player_dict)):
        player = player_dict[i]
        player_dict[i] = player_movement(a_board1, player)
        if player_dict[i] == -1:
            print(f"Player {i} has won!")
            break


