import random
from time import sleep
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['AlternativeAssessment']
top_scores = db['SnakesAndLadders']
top_3 = []
scores_loopble = top_scores.find()
for item in scores_loopble:
    small = 10**10000
    if item["score"] < small:
        top_3.append(item)
        small = item["score"]


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
    elif i == 87:
        a_board1.append(30)
    else:
        a_board1.append(0)
b_board1 = []
for i in range(100):
    if i % 6 != 5:
        b_board1.append(2)
    else:
        b_board1.append(0)

c_board1 = [0]*100
for i in range(100):
    if random.randint(0, 5) != 0:
        continue
    if random.randint(0, 3) == 0 and i < 30:
        c_board1[i] = i+random.randint(1, 20)
    elif random.randint(0, 2) == 0 and i > 30:
        c_board1[i] = i-random.randint(1, 20)


def die():
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


def player_control(player_dict, chosen_board, auto, silent, mainiac):
    if chosen_board == "a":
        board = a_board1
    elif chosen_board == "b":
        board = b_board1
    else:
        board = c_board1

    for j in range(len(player_dict)):
        player = player_dict[j]

        if not auto:
            input(f"Player {j+1}, press enter to roll the dice")
        pos_to_move = player_movement(board, player)
        player_dict[j] = pos_to_move
        if mainiac:
            sleep(3)
        if not silent:
            print(f"Player {j+1} is on position {pos_to_move+1}")
        if player_dict[j] == -1:
            print(f"Player {j+1} has won!")
            return True
    return False


def print_board(board):
    for j in range(len(board)):
        if board[j] == 0:
            print(j+1, end="|")
        else:
            print(f"#{board[j]+1}", end="|")
        if j % 10 == 9:
            print("|")


def print_high_scores():
    for score in top_3:
        print(f"{score['player']} - {score['score']}")


def main():
    player_count = int(input("How many players? "))
    player_dict = {j: 0 for j in range(player_count)}
    chosen_board = input("Which board do you want to play on? (a/b/c) ")
    if chosen_board != "a" and chosen_board != "b" and chosen_board != "c":
        print("Invalid input, please try again")
        return
    if chosen_board == "a":
        print_board(a_board1)
    elif chosen_board == "b":
        print_board(b_board1)
    elif chosen_board == "c":
        print_board(c_board1)
    auto = input("Do you want to play automatically? (y/n) ") == "y"
    silent = input("Do you want to play silently? (y/n) ") == "y"
    mainiac = input("Are you insane (or a masochist)? (y/n) ") == "y"
    print_top_scores = input("Do you want to see the top scores? (y/n) ") == "y"
    if print_top_scores:
        print_high_scores()
    turn_count = 0
    while True:
        turn_count += 1
        if player_control(player_dict, chosen_board, auto, silent, mainiac):
            break
    print(f"It took {turn_count} turns to win")
    for score in top_3:
        if score['score'] > turn_count:
            player_name = input("You topped a previous record! What is your name? ")
            top_scores.insert_one({'player': player_name, 'score': turn_count})
            break
    print_high_scores()


if __name__ == '__main__':
    main()
