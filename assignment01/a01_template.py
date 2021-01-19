import numpy as np
from sklearn import preprocessing

# color output labels by order
color_labels = ['AMBER', 'BLACK', 'GOLD', 'GREEN', 'LILAC', 'PINK', 'RED', 
             'SILVER', 'WHITE']

# creating color output set to empty string. 
color_output = ""             

# Create label encoder and fit the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(color_labels)

# show the color label for the user to reference. 
print(color_labels)

# asking the user to enter a number or a color to print out.  
input_string = input("Please enter a number from 0 - 8 OR color: ")
input_val = str(input_string) 

# Checking if input string is holding in the color label. 
# AND using the encoder classes__ for holding its label for each class.
if input_string in encoder.classes_: 
    color_output = input_string
else: 
    color_output = color_labels[int(input_val)] 
        
# Displays the output
print(color_output, encoder.transform([color_output])) 


 