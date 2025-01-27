import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

import chardet

# I needed the following code to know the codification of my document, once this code tells us the specific codification we won't need it anymore
#with open("DOGE-USD.csv","rb") as file:
    #result = chardet.detect(file.read())
    #print(result)

import csv
with open("DOGE-USD.csv","r", encoding="ascii") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = pd.read_csv("DOGE-USD.csv","r", encoding="ascii")
print(data)

