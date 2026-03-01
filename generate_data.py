"""
Generate synthetic house price dataset for demonstration
"""
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 1000 samples
n_samples = 1000

# Generate features
data = {
    'square_feet': np.random.randint(800, 5000, n_samples),
    'bedrooms': np.random.randint(1, 7, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples),
    'age': np.random.randint(0, 100, n_samples),
    'garage_spaces': np.random.randint(0, 4, n_samples),
    'lot_size': np.random.randint(2000, 20000, n_samples),
    'neighborhood_score': np.random.uniform(1, 10, n_samples),
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate price based on features with some noise
# Price formula: base price + contributions from features + noise
base_price = 50000
price = (
    base_price +
    df['square_feet'] * 150 +  # $150 per square foot
    df['bedrooms'] * 15000 +   # $15k per bedroom
    df['bathrooms'] * 10000 +  # $10k per bathroom
    -df['age'] * 500 +         # Depreciation
    df['garage_spaces'] * 8000 + # $8k per garage space
    df['lot_size'] * 5 +       # $5 per sq ft of lot
    df['neighborhood_score'] * 20000 + # Neighborhood quality
    np.random.normal(0, 30000, n_samples)  # Random noise
)

df['price'] = price.round(2)

# Ensure no negative prices
df['price'] = df['price'].clip(lower=50000)

# Save to CSV
df.to_csv('data/house_prices.csv', index=False)

print(f"Dataset created with {n_samples} samples")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nDataset statistics:")
print(df.describe())
