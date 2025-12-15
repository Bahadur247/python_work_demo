import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Shalimar facebook leds.xlsx")

# print(data)

data.drop(columns="Labels", inplace=True)
# print(data.isnull().sum())
print(data.info())

data["Created"] = data["Created"].astype(str)
lenghts = data["Created"].str.len()

not_date = data[lenghts < 17]
date = data[lenghts >= 17]

print("dates : ", (lenghts >= 17).sum())
print("not dates : ", (lenghts<17).sum())

