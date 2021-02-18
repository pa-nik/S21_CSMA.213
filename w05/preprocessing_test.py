import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]]) 
print('input data:')
print(input_data)

# binarize input data
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print('binarized input data:')
print(data_binarized)

# normalize data between -1 and 1
data_normalized_l1 = preprocessing.normalize(input_data, norm = "l1")
print('normalized input data:')
print(data_normalized_l1)
