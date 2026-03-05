import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def generate_data():
    data = [
    {
        "surface": 10,
    },    
    {
        "surface": 40,
    },    
    {
        "surface": 80,
    },   
    {
        "surface": 70,
    },    
    {
        "surface": 200,
    },   
    {
        "surface": 120,
    },   
    {
        "surface": 79,
    },    
    {
        "surface": 39,
    },    
    {
        "surface": 28,
    },    {
        "surface": 15,
    },
    ]
    for item in data:
        item["price"] = item["surface"] * 3000 + round(random.random() * 100, 2)
    
    return data

data = generate_data()

print(data)

df = pd.DataFrame.from_dict(data)
print(df.head())

mean = df.mean(axis=0)
max = df.max(axis=0)
min = df.min(axis=0)

plt.plot(df["surface"], df["price"])
plt.show()




