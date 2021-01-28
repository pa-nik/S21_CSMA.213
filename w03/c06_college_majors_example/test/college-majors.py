import numpy as np
import pandas as pd
import os 


s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(s)


df = pd.DataFrame(np.random.randn(9, 4), columns = list('ABCD'))
# print(df)
# print(df.head())
# print (df['A'])


cd = os.getcwd()
data_set = pd.read_csv(cd + '\college-majors.csv')
# print(data_set)
# print(data_set['Major'])

# for index,row in data_set.iterrows():
#     print(row['Major'])

with open('college-majors.txt', 'w') as filename:
    for index,row in data_set.iterrows():
        print('writing to file...' + row['Major'])
        filename.write('%s\n' % row['Major'])