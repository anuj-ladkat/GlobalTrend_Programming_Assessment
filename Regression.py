import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Fetch the California Housing dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = data.target

# Define features (X) and target (y)
X = df.drop(columns=['Target'])
y = df['Target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Optional: Add polynomial features to capture non-linear relationships
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Evaluate the model using cross-validation
cv_scores = cross_val_score(model, X_train_poly, y_train, cv=10, scoring='neg_mean_squared_error')
mean_cv_score = -cv_scores.mean()
print(f"Cross-Validation Mean Squared Error: {mean_cv_score}")

# Make predictions on the test set
y_pred = model.predict(X_test_poly)

# Evaluate the model's performance on the test set
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation results
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Example usage: Print first 5 actual vs predicted values
print("\nFirst 5 Actual vs Predicted Values:")
for actual, predicted in zip(y_test[:5], y_pred[:5]):
    print(f"Actual: {actual:.2f}, Predicted: {predicted:.2f}")
