import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import warnings
warnings.filterwarnings('ignore')

import chardet

# I needed the following code to know the codification of my document, once this code tells us the specific codification we won't need it anymore

with open("MU DATA","rb") as file:
    result = chardet.detect(file.read())
    print(result)

import csv
with open("MU DATA","r", encoding="ascii") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = pd.read_csv("MU DATA","r", encoding="ascii")
print(data)
