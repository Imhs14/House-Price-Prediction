"""
Model training and evaluation
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import json

class HousePriceModel:
    """Linear Regression model for house price prediction"""
    
    def __init__(self):
        self.model = LinearRegression()
        self.metrics = {}
        
    def train(self, X_train, y_train):
        """Train the linear regression model"""
        print("Training model...")
        self.model.fit(X_train, y_train)
        print("Model training completed!")
        
    def predict(self, X):
        """Make predictions"""
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance"""
        y_pred = self.predict(X_test)
        
        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        self.metrics = {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2_score': r2
        }
        
        print(f"\nModel Performance Metrics:")
        print(f"Mean Squared Error (MSE): ${mse:,.2f}")
        print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")
        print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
        print(f"R² Score: {r2:.4f}")
        
        return self.metrics
    
    def get_feature_importance(self, feature_names):
        """Get feature coefficients"""
        coefficients = pd.DataFrame({
            'Feature': feature_names,
            'Coefficient': self.model.coef_
        }).sort_values('Coefficient', ascending=False)
        
        return coefficients
    
    def save_model(self, path='models/house_price_model.pkl'):
        """Save the trained model"""
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")
    
    def save_metrics(self, path='models/metrics.json'):
        """Save model metrics"""
        with open(path, 'w') as f:
            json.dump(self.metrics, f, indent=4)
        print(f"Metrics saved to {path}")
    
    def load_model(self, path='models/house_price_model.pkl'):
        """Load a saved model"""
        self.model = joblib.load(path)
        print(f"Model loaded from {path}")
        return self.model
