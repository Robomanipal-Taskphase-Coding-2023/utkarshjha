import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading data from a file
df = pd.read_csv("linear_regression_dataset.csv")
df.fillna(df.mean(), inplace=True)
a='APRDRG'
# Feature Scaling (Normalization)
df[a] = (df[a] - df[a].mean()) / df[a].std()
df['TOTCHG'] = (df['TOTCHG'] - df['TOTCHG'].mean()) / df['TOTCHG'].std()


import numpy as np

def gradient_descent(m, b, points, learning_rate):
    x = points[a].values
    y = points['TOTCHG'].values
    n = len(points)

    # Calculate predictions and errors
    predictions = m * x + b
    errors = y - predictions

    # Compute gradients
    m_gradient = (-2 / n) * np.dot(x, np.clip(errors, -1e15, 1e15))
    b_gradient = (-2 / n) * np.sum(np.clip(errors, -1e15, 1e15))

    # Update parameters
    m -= learning_rate * m_gradient
    b -= learning_rate * b_gradient

    # Clip parameters to avoid numerical instability
    m = np.clip(m, -1e15, 1e15)
    b = np.clip(b, -1e15, 1e15)

    # Check for NaN values in updated parameters
    if np.isnan(m) or np.isnan(b):
        raise ValueError("Oops! Something went wrong. Try changing the learning rate.")

    return m, b



# Initializing variables
m = 0
b = 0
learning_rate = 0.1
iterations = 10000

# Running Gradient Descent
for i in range(iterations):
    m, b = gradient_descent(m, b, df, learning_rate)

    #if i % 100 == 0:
       # print(f"At iteration {i}: Slope (m) = {m}, Intercept (b) = {b}")

# Final Results
print("\nFinal Results:")
print("Slope (m):", m)
print("Intercept (b):", b)

# Plotting the regression line
plt.scatter(df.APRDRG, df.TOTCHG)
plt.plot(df[a], m * df[a] + b, color="red")
plt.xlabel(a)
plt.ylabel('TOTCHG')
plt.title('Linear Regression')
plt.show()
