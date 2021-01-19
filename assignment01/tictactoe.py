import numpy as np
import random


# Creates blank 3x3 array. Randomizes who goes first.
def init():
    global board_arr
    global my_arr
    
    # 0's acts as O's
    # 1's acts as X's
    # 2's acts as placeholders for blank spots
    board_arr = np.array([[3, 3, 3],
                          [3, 3, 3],
                          [3, 3, 3]])
    my_arr = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])
    
    global user_num
    global comp_num
    
    # Flip a coin to see who goes first with X's
    coin_flip = np.random.randint(0, 2)
    if  coin_flip == 0:
        user_num = 0
        comp_num = 1
        print("Computer goes first. Your letter is O.")
        comp_turn()
        
    elif coin_flip == 1:
        user_num = 1
        comp_num = 0
        print("You go first. Your letter is X.")
        user_turn()

        
# Converts internal numpy array into a visual board.       
def display_board():
    board_list = []
    
    # loops through flattened board array to scan for 0's, 1's and 3's
    # converts them into O's, X's, and blank spots
    internal_arr = board_arr.flatten()
    for i in range(0, 9):
       if internal_arr[i] == 0:
           board_list.append('O')
       elif internal_arr[i] == 1:
           board_list.append('X')
       elif internal_arr[i] == 3:
           board_list.append(' ')
       else:
           raise Exception("display_board Error")
    
    # inputs O's, X's, and blank spots into an ASCII tictactoe board
    print("""
 {} | {} | {}
---+---+---
 {} | {} | {}
---+---+---
 {} | {} | {}
""".format(*board_list))
    
    
def return_open_slots():

    open_slots = []

    bool_arr = (board_arr == 3)
    flat_bool_arr = bool_arr.flatten()
    
    # is spot taken by 3's? If so, then spot is open.
    # appends (i + 1) because inputs are indexed to 1
    for i in range(0, len(flat_bool_arr)):
        if flat_bool_arr[i] == True:
            open_slots.append(i + 1)
            
    return open_slots


def terminate(last_played_num):

    if last_played_num == user_num:
        print("You win!")
    elif last_played_num == comp_num:
        print("You lost!")
    elif last_played_num == "Tie!":
        print("Tie!")
        
    input("Play again? \nPress Enter to play again.")
    init()
        
def check_for_winner(last_played_num):

    
    if return_open_slots == []:
    # Checks if no open slots
        terminate("Tie!")
        
    for i in range(0, 3):
    # Checks rows and columns for match
        rows_win = (board_arr[i, :] == last_played_num).all()
        cols_win = (board_arr[:, i] == last_played_num).all()
        
        if rows_win or cols_win:
            terminate(last_played_num)
            
    diag1_win = (np.diag(board_arr) == last_played_num).all()
    diag2_win = (np.diag(np.fliplr(board_arr)) == last_played_num).all()
    
    if diag1_win or diag2_win:
    # Checks both diagonals for match
        terminate(last_played_num)
            
    next_turn(last_played_num)
    
    
def next_turn(last_played_num):
    if last_played_num == user_num:
        comp_turn()
    elif last_played_num == comp_num:
        user_turn()


def place_letter(current_num, current_input):

    index = np.where(my_arr == current_input)
    board_arr[index] = current_num

    

def user_turn():
    display_board()
    
    user_input = input("Pick an open slot from 1-9: ")
    user_input = int(user_input)
    
    if user_input in return_open_slots():
        place_letter(user_num, user_input)
    else:
        print("Oops, that's not a open slot(s).")
        user_turn()
        
    check_for_winner(user_num)
    

# A feature I added (I did not know you want only the individual to play by itself,
# so I added a feature to play with computer with random module.)
def comp_turn():
# Randomly chooses from open_slots to place its letter    
    open_slots = return_open_slots()
    comp_input = random.choice(open_slots)
    place_letter(comp_num, comp_input)
    check_for_winner(comp_num)
    

init()