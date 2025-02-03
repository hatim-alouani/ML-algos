import numpy as np

print("moindres caree (methode)")

# math formulat : 
# y = a * x + a2 * x2 + b
# Calculate means
# a = ∑(x - x_mean) * (y - y_mean)
# b = y_mean - (a1 * x1_mean) (a2 * x2_mean)

x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([2, 3, 4, 5, 6])
y = np.array([10, 14, 18, 22, 26])

n = len(y)
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
y_mean = np.mean(y)

a1 = np.sum((x1 - x1_mean) * (y - y_mean)) / np.sum((x1 - x1_mean) ** 2)
a2 = np.sum((x2 - x2_mean) * (y - y_mean))/ np.sum((x2 - x2_mean) ** 2)
b = y_mean - (a1 * x1_mean) - (a2 * x2_mean)

val1 = 5
val2 = 6

print(f"result  : {a1 * val1 + a2 * val2 + b}")