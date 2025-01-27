import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import warnings
warnings.filterwarnings('ignore')

import chardet

# I need the following code to know the codification of my document, once this code tells us the specific codification we won't need it anymore#with open("MU DATA.csv","rb") as file:
    #result = chardet.detect(file.read())
    #print(result)

import csv
with open("MU DATA.csv", encoding="ascii") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = pd.read_csv("MU DATA.csv", encoding="ascii")
print(data)

arr = np.array([1, 2, 3])
arr_tuple = tuple(arr)  # Convert ndarray to tuple
my_set = {arr_tuple}  # Now this works
print(my_set)

plt.figure(figsize=(15,5))
plt.plot(data)
plt.title('Micron technology price.', fontsize=20)
plt.ylabel('price in dollars.')
plt.show()


