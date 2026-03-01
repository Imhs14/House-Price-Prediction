"""
Configuration file for House Price Prediction project
"""

# Data Generation Parameters
DATA_CONFIG = {
    'n_samples': 1000,
    'random_seed': 42,
    'test_size': 0.2,
}

# Feature Ranges
FEATURE_RANGES = {
    'area': (500, 5000),        # Square feet
    'bedrooms': (1, 6),
    'bathrooms': (1, 5),
    'age': (0, 50),             # Years
    'garage': (0, 4),
    'location_score': (1, 10),  # 1-10 scale
    'has_pool': (0, 2),         # Binary
    'has_garden': (0, 2),       # Binary
    'floors': (1, 4),
}

# Price Calculation Weights
PRICE_WEIGHTS = {
    'area': 150,
    'bedrooms': 15000,
    'bathrooms': 12000,
    'age': -2000,
    'garage': 8000,
    'location_score': 10000,
    'has_pool': 25000,
    'has_garden': 15000,
    'floors': 20000,
    'noise_std': 50000,
}

# Model Parameters
MODEL_CONFIG = {
    'model_type': 'LinearRegression',
    'scale_features': True,
    'random_state': 42,
}

# File Paths
PATHS = {
    'data_dir': 'data',
    'model_dir': 'models',
    'full_dataset': 'data/house_prices.csv',
    'train_data': 'data/train.csv',
    'test_data': 'data/test.csv',
    'model_file': 'models/house_price_model.pkl',
    'scaler_file': 'models/scaler.pkl',
    'feature_names_file': 'models/feature_names.pkl',
    'metrics_file': 'models/metrics.csv',
}

# Visualization Settings
VIZ_CONFIG = {
    'figure_size': (15, 12),
    'dpi': 300,
    'style': 'whitegrid',
    'color_palette': 'husl',
}

# Streamlit App Settings
APP_CONFIG = {
    'title': 'House Price Prediction System',
    'icon': '🏠',
    'layout': 'wide',
    'default_area': 2000,
    'default_bedrooms': 3,
    'default_bathrooms': 2,
    'default_age': 10,
    'default_garage': 2,
    'default_location_score': 7.0,
    'default_floors': 2,
}
