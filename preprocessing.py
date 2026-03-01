"""
Data preprocessing utilities
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

class DataPreprocessor:
    """Handle data loading and preprocessing"""
    
    def __init__(self, data_path='data/house_prices.csv'):
        self.data_path = data_path
        self.scaler = StandardScaler()
        self.feature_names = None
        
    def load_data(self):
        """Load data from CSV"""
        df = pd.read_csv(self.data_path)
        print(f"Data loaded: {df.shape}")
        return df
    
    def get_features_target(self, df):
        """Separate features and target variable"""
        X = df.drop('price', axis=1)
        y = df['price']
        self.feature_names = X.columns.tolist()
        return X, y
    
    def split_data(self, X, y, test_size=0.2, random_state=42):
        """Split data into train and test sets"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        print(f"Train set: {X_train.shape}, Test set: {X_test.shape}")
        return X_train, X_test, y_train, y_test
    
    def scale_features(self, X_train, X_test):
        """Scale features using StandardScaler"""
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled
    
    def save_scaler(self, path='models/scaler.pkl'):
        """Save the fitted scaler"""
        joblib.dump(self.scaler, path)
        print(f"Scaler saved to {path}")
    
    def load_scaler(self, path='models/scaler.pkl'):
        """Load a saved scaler"""
        self.scaler = joblib.load(path)
        print(f"Scaler loaded from {path}")
        return self.scaler
