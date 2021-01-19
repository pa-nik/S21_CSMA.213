import numpy as np
from sklearn import preprocessing

input_num_color = input(f"Input a number from 0 - 8 or a color: ")

input_labels = ['amber', 'black', 'gold', 'green', 'lilac', 'pink', 'red', 'silver', 'white']    
 
# Create label encoder and fit the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

if input_num_color in input_labels:
    encoded_values = encoder.transform([input_num_color])    # changes to nums
    print(encoded_values)
else:
    input_num_color = int(input_num_color)
    decoded_list = encoder.inverse_transform([input_num_color])    # changes to words
    print(decoded_list)
