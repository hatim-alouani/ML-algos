import numpy as np
import pandas as pd


print("multiple linear regression (Methode)")

#math formula
#y = a1 * x1 + a2 * x2 + b
#a1 = n⋅∑(x1.y)−∑(x1)⋅∑(y) / n⋅∑(x1**2)−∑(x1)**2
#a2 = n⋅∑(x2.y)−∑(x2)⋅∑(y) / n⋅∑(x2**2)−∑(x2)**2
#a3 = n⋅∑(x3.y)−∑(x3)⋅∑(y) / n⋅∑(x3**2)−∑(x3)**2
#b = (∑(y) − a1⋅∑(x1) - a2⋅∑(x2) - a3⋅∑(x3)) / n


data = pd.read_csv("50_Startups.csv")
x1 = data["R&D Spend"]
x2 = data["Administration"]
x3 = data["Marketing Spend"]
y = data["Profit"]
n = len(y)

a1 = (n * np.sum(x1 * y) - np.sum(x1) * np.sum(y)) / (n * np.sum(x1**2) - np.sum(x1)**2)
a2 = (n * np.sum(x2 * y) - np.sum(x2) * np.sum(y)) / (n * np.sum(x2**2) - np.sum(x2)**2)
a3 = (n * np.sum(x3 * y) - np.sum(x3) * np.sum(y)) / (n * np.sum(x3**2) - np.sum(x3)**2)
b = (np.sum(y) - (a1 * np.sum(x1)) - (a2 * np.sum(x2)) - (a3 * np.sum(x3))) / n

val1 = 134615.46
val2 = 147198.87
val3 = 127716.82

print(f"result  : {a1 * val1 + a2 * val2 + a3 * val3 + b}")

