import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

# Set random seed for reproducibility
np.random.seed(42)

# Generate linear regression data
n_samples = 100
n_features = 1
X, y = make_regression(n_samples=n_samples, n_features=n_features, noise=10, random_state=42)


# Create a DataFrame
X_df = pd.DataFrame(X, columns=[f'feature{i}' for i in range(1, n_features + 1)])
y_df = pd.DataFrame({'output': y})


# Save to CSV
X_df.to_csv('X.csv', index=False)
y_df.to_csv('y.csv', index=False)

print("CSV files generated successfully.")