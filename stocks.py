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

#x = np.array([2, 3, 6, 7, 8, 10, 13, 14, 15])
#y = np.array([87.33, 89.87, 99.26, 101.91, 99.41, 99.34, 95.06, 97.36, 103.19])

Días = data["DATE"]
Precio = data["CLOSE"]

plt.figure(figsize=(10,5))
plt.xlabel(Días)
plt.plot(Días, Precio)
plt.title('Micron technology price.', fontsize=20)
plt.ylabel(Precio)
plt.xlim(0, 15)
plt.yticks(np.arange(80, 120, 5))
plt.ylim(80, 115)
plt.show()



