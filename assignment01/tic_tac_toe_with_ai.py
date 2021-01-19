import numpy as np
import random


# I think np arrays only take ints and floats so I can't do X's and O's
def print_game_info():
    print("Marks are based on player order.\n For example, if you go first, your marks will be a '1'\n")

# create an empty board
def create_empty_board():
    return np.zeros((3,3))

# place a 1 or 2 (based on player order) on the board
def place(board, player, place_pos):
    if board[place_pos[0], place_pos[1]] == 0:
        board[place_pos[0], place_pos[1]] = player
    else:
        print("Cannot place in that position.")
    return board

# define moves for AI for first and second
def ai_possible_moves(board):
    empty = np.where(board == 0)
    ai_goes_first = empty[0].tolist()
    ai_goes_second = empty[1].tolist()
    return [x for x in zip(ai_goes_first, ai_goes_second)]

# AI chooses a random move
def place_random_mark(board, player):
    empty = ai_possible_moves(board)
    return place(board, player, random.choice(empty))

# will check rows for a win
def check_row_wins(board, player):
    return np.any((np.all(board == player, axis=1)))

# will check columns for a win
def check_column_wins(board, player):
    return np.any((np.all(board==player, axis=0)))

# will check diagonals for a win
def check_diagonal_wins(board, player):
    diag1 = np.array([board[0,0], board[1,1], board[2,2]])
    diag2 = np.array([board[0,2], board[1,1], board[2,0]])
    return np.all(diag1 == player) or np.all(diag2 == player)

# check any/all possible wins at the end of each turn
def check_possible_wins(board, players):
    winner = 0
    for player in players:
        if check_row_wins(board, player):
            winner = player
        elif check_column_wins(board, player):
            winner = player
        elif check_diagonal_wins(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
   
    board = create_empty_board()
    print("Current board state: \n")
    print(board)
    print("\nType in the row and column to place your mark.\nFor example, to place in the middle, type 2,2 (no spaces plz)\n")
    game_order = int(input("Do you want to go first or second? (1/2): "))

    if game_order == 1:
        player1 = 1
        ai_player = 2
        players = [player1, ai_player]
    else:
        player1 = 2
        ai_player = 1
        players = [ai_player, player1]
    print(f"You are player {game_order}")
    winner = 0
    while winner == 0:
        for player in players:
            if player == game_order:
                place_pos = input("What row/column do you want to place your mark in? (row, col): ")
                print(f"You placed it in {place_pos}")
                place_pos = int(place_pos[0])-1, int(place_pos[2])-1
                place(board, player1, place_pos)
                print(board)
            else:
                print("AI move:")
                place_random_mark(board, player)
                print(board)
            winner = check_possible_wins(board, players)
            if winner > 0:
                print("YOU WIN!!!")
            elif winner == -1:
                print("YOU TIED!!!")
                break
    return winner

print_game_info()
play_game()
