import numpy as np
from sklearn import preprocessing
from ttt import TicTacToe

colors = ["amber", "black", "gold", "green", "lilac", "pink", "red", "silver", "white"]

encoder = preprocessing.LabelEncoder()
encoder.fit(colors)

input_string = input(f"type in a number [0 - 8] OR a color [{', '.join(colors)}]: ")

selected_color = None

# create a Python program that accepts a number 0 - 8 as input and outputs the color label associated with this number based on color assignments shown on the game board above. 
# Write a Python program that performs the opposite procedure of decoding a color label to a number value associated with it. 
# combine the programs above so that you could input either number or color and get a corresponding encoded/decoded output.  This means your program would ask the user to enter a number OR color and act accordingly.

if input_string.lower() in encoder.classes_: # could be if input_string in colors:
    selected_color = input_string
else:
    try:
        selected_color = colors[int(input_string)]
    except:
        print("Error: invalid input.")
        exit(0)

print("You selected",selected_color,"@ index",encoder.transform([selected_color]))

# Tic Tac Toe
# write a modified program that uses array objects available in numpy library to keep track of played tic-tac-toe board positions and print them out to the console, allowing you to play the game by inputting numbers corresponding to the positions on the board.  
game = TicTacToe()
game.start()