import numpy as np
from sklearn import preprocessing

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

input_labels = ['amber', 'black', 'gold', 'green', 'lilac', 'pink', 'red', 'silver', 'white']
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#############################################################################################################################################################

# Part 1

# encoded_values = []
# input_string = input("type in a number 0 - 8: ")
# input_val = int(input_string)
# test1 = encoded_values.append(input_val)
# decoded_list = encoder.inverse_transform(encoded_values)
# print("you typed: ", list(decoded_list))

# Part 2

# decoded_values = []
# input_string = input("type a color: ")
# input_val = str(input_string)
# test2 = decoded_values.append(input_val)
# decoded_list = encoder.transform(decoded_values)
# print("you typed: ", list(decoded_list))

#############################################################################################################################################################

# Part 3

def show_board():

    print(board[1], '|', board[2], '|', board[3])
    print('-----------')
    print(board[8], '|', board[0], '|', board[4])
    print('-----------')
    print(board[7], '|', board[6], '|', board[5])

def player_x():

    input_string = input("Player 1 type in a number 0 - 8: ")
    input_val = int(input_string)        

    if board[input_val] != 'X' and board[input_val] !='O':
        board[input_val] = 'X' 

    else:
        print('taken')

def player_o():
    input_string = input("Player 2 type in a number 0 - 8: ")
    input_val = int(input_string)

    if board[input_val] != 'O' and board[input_val] !='X':
        board[input_val] = 'O' 

    else:
        print('taken')


while True:
    for i in range (0,8):
        player_x()
        show_board()
        player_o()
        show_board()
