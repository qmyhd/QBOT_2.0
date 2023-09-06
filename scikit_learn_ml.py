from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Generate some sample data
X, y = np.arange(10).reshape(-1, 1), np.array([1, 3, 2, 3, 5, 6, 7, 8, 9, 10])

# Split the data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

print(f'Predicted values: {y_pred}')
print(f'Actual values: {y_test}')
 
try:
    model.fit(X_train, y_train)
except Exception as e:
    print(f"An error occurred while fitting the model: {e}")

try:
    y_pred = model.predict(X_test)
except Exception as e:
    print(f"An error occurred while making predictions: {e}")
