import numpy as np
from sklearn import preprocessing


#This is part one

# input_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
# output_labels = ['Amber', 'Black', 'Gold', 'Green', 'Lilac', 'Pink', 'Red', 'Silver', 'White']

# input_string = input("type in a number 0 - 8: ")
# input_val = int(input_string)
# print("you typed: ", input_val)

# encoder = preprocessing.LabelEncoder()
# encoder.fit(input_labels)

# print(input_val, '-->', output_labels[input_val])

#############################################################################################################################################################

#This is part two

# output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
# input_labels = ['Amber', 'Black', 'Gold', 'Green', 'Lilac', 'Pink', 'Red', 'Silver', 'White']


# input_string = input("type in a color: ")
# input_val = int(input_string)
# print("you typed: ", input_string)

# encoder = preprocessing.LabelEncoder()
# encoder.fit(input_labels)


# print(input_string, '-->', int(encoder.transform([input_string])))

#############################################################################################################################################################

#This is part three (the tic tac toe game)


tttBoard = np.array(('1', '2', '3', 
                    '8', '0', '4',
                    '7', '6', '5'))

emptyBoard = np.array((' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' '))

empty = ' '

board_keys = []

for key in tttBoard:
    board_keys.append(key)

#This is a function that we can call on to keep printing the board after each player's turn so it's convenient

def printBoard(board):
    print(emptyBoard[1] + '|' + emptyBoard[2] + '|' + emptyBoard[3])
    print('-+-+-') #This just helps create the board, mostly just too make it look good
    print(emptyBoard[8] + '|' + emptyBoard[0] + '|' + emptyBoard[4])
    print('-+-+-') #This just helps create the board, mostly just too make it look good
    print(emptyBoard[7] + '|' + emptyBoard[6] + '|' + emptyBoard[5])
    print("\n")

    

def game():

    currentTurn = 'X' #X goes first, not sure if that's like an actual rule but too bad player O deal with it
    count = 0 


    for i in range(10):
        printBoard(tttBoard)
        print("It's your turn, player " + currentTurn)

        move = int(input())        

        if emptyBoard[move] == empty:
            tttBoard[move] = currentTurn
            emptyBoard[move] = currentTurn
            count += 1
        else:
            print("That place is already filled.\nPlease pick another square")
            continue

        # This will check if someone has won after each turn starting from turn 5 because it takes a minimum of 5 turns to win tic tac toe 
        if count >= 5:
            if emptyBoard[1] == emptyBoard[2] == emptyBoard[3] != empty: # win across the top
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")                
                break
            elif emptyBoard[8] == emptyBoard[0] == emptyBoard[4] != empty: # win across the middle
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break
            elif emptyBoard[7] == emptyBoard[6] == emptyBoard[5] != empty: # win across the bottom
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break
            elif emptyBoard[1] == emptyBoard[8] == emptyBoard[7] != empty: # win down the left side
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break
            elif emptyBoard[2] == emptyBoard[0] == emptyBoard[6] != empty: # win down the middle
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break
            elif emptyBoard[3] == emptyBoard[4] == emptyBoard[5] != empty: # win down the right side
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break 
            elif emptyBoard[3] == emptyBoard[0] == emptyBoard[7] != empty: # win on the diagonal (top-right --> bottom-left)
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break
            elif emptyBoard[1] == emptyBoard[0] == emptyBoard[5] != empty: # win on the diagonal (top-left --> bottom-right)
                printBoard(tttBoard)
                print("\nGame Over.\n")                
                print(" **** " +currentTurn + " won. ****")
                break 

        # This checks to see if the board is full, if it is then the game will be declared a tie.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # This changes the turn between X's turn and O's turn
        if currentTurn =='X':
            currentTurn = 'O'
        else:
            currentTurn = 'X'        
    
game()    









