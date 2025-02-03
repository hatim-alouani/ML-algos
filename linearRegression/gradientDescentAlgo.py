import numpy as np

print("gradient descent (optimization algorithm)")

# math formulat
# y = a * x + b
# ∂J/∂a = −2/n * ∑x(y − y_pred)
# ∂J/∂b = −2/n * ∑(y − y_pred)
# a = a - learning_rate * ∂J/∂a
# b = b - learning_rate * ∂J/∂b

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 14, 18, 22, 26])

a = 0
b = 0
n = len(y)

def gradient_descent(x, y, a, b, learning_rate, iterations):
    for _ in range(iterations):
        y_pred = a * x + b
        da = -(2/n) * sum(x * (y - y_pred))
        db = -(2/n) * sum(y - y_pred)
        a = a - learning_rate * da
        b = b - learning_rate * db
    
    return a, b

learning_rate = 0.01
iterations = 1000

a, b = gradient_descent(x, y, a, b, learning_rate, iterations)

val = 5

print(f"result  : {(a * val)+ b}")
