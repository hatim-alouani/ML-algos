import numpy as np
import pandas as pd

print("simple linear regression (Methode)")

#math formula
#y = a * x + b
#a = n⋅∑(x.y)−∑(x)⋅∑(y) / n⋅∑(x**2)−∑(x)**2
#b = ∑(y)−a⋅∑(x) / n

data = pd.read_csv("Salary_Data.csv")

x = data["YearsExperience"].values
y = data["Salary"].values
n = len(y)

a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
b = (np.sum(y) - a * np.sum(x)) / n

val = 1.1

print(f"result  : {(a * val)+ b}")
