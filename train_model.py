"""
Train Linear Regression model for house price prediction
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

class HousePriceModel:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.feature_names = None
        
    def train(self, X_train, y_train):
        """Train the model"""
        print("Training Linear Regression model...")
        
        # Store feature names
        self.feature_names = X_train.columns.tolist()
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Train model
        self.model.fit(X_train_scaled, y_train)
        
        print("Training completed!")
        
    def predict(self, X):
        """Make predictions"""
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance"""
        predictions = self.predict(X_test)
        
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        metrics = {
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'R2': r2
        }
        
        return predictions, metrics
    
    def get_feature_importance(self):
        """Get feature coefficients"""
        return dict(zip(self.feature_names, self.model.coef_))
    
    def save(self, model_path='models/house_price_model.pkl', scaler_path='models/scaler.pkl'):
        """Save model and scaler"""
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        joblib.dump(self.feature_names, 'models/feature_names.pkl')
        print(f"Model saved to {model_path}")
        print(f"Scaler saved to {scaler_path}")
    
    @classmethod
    def load(cls, model_path='models/house_price_model.pkl', scaler_path='models/scaler.pkl'):
        """Load trained model and scaler"""
        instance = cls()
        instance.model = joblib.load(model_path)
        instance.scaler = joblib.load(scaler_path)
        instance.feature_names = joblib.load('models/feature_names.pkl')
        return instance


def main():
    print("=" * 60)
    print("HOUSE PRICE PREDICTION - MODEL TRAINING")
    print("=" * 60)
    
    # Load data
    print("\n1. Loading data...")
    train_df = pd.read_csv('data/train.csv')
    test_df = pd.read_csv('data/test.csv')
    
    # Separate features and target
    X_train = train_df.drop('price', axis=1)
    y_train = train_df['price']
    X_test = test_df.drop('price', axis=1)
    y_test = test_df['price']
    
    print(f"   Training samples: {len(X_train)}")
    print(f"   Testing samples: {len(X_test)}")
    print(f"   Features: {X_train.columns.tolist()}")
    
    # Initialize and train model
    print("\n2. Training model...")
    model = HousePriceModel()
    model.train(X_train, y_train)
    
    # Evaluate on training data
    print("\n3. Training Set Performance:")
    train_predictions, train_metrics = model.evaluate(X_train, y_train)
    print(f"   R² Score: {train_metrics['R2']:.4f}")
    print(f"   RMSE: ${train_metrics['RMSE']:,.2f}")
    print(f"   MAE: ${train_metrics['MAE']:,.2f}")
    
    # Evaluate on test data
    print("\n4. Test Set Performance:")
    test_predictions, test_metrics = model.evaluate(X_test, y_test)
    print(f"   R² Score: {test_metrics['R2']:.4f}")
    print(f"   RMSE: ${test_metrics['RMSE']:,.2f}")
    print(f"   MAE: ${test_metrics['MAE']:,.2f}")
    
    # Feature importance
    print("\n5. Feature Importance (Coefficients):")
    feature_importance = model.get_feature_importance()
    for feature, coef in sorted(feature_importance.items(), key=lambda x: abs(x[1]), reverse=True):
        print(f"   {feature}: {coef:,.2f}")
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Model Performance Analysis', fontsize=16)
    
    # 1. Actual vs Predicted (Test Set)
    axes[0, 0].scatter(y_test, test_predictions, alpha=0.5, color='blue')
    axes[0, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    axes[0, 0].set_xlabel('Actual Price ($)')
    axes[0, 0].set_ylabel('Predicted Price ($)')
    axes[0, 0].set_title('Actual vs Predicted Prices (Test Set)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Residuals plot
    residuals = y_test - test_predictions
    axes[0, 1].scatter(test_predictions, residuals, alpha=0.5, color='green')
    axes[0, 1].axhline(y=0, color='r', linestyle='--', lw=2)
    axes[0, 1].set_xlabel('Predicted Price ($)')
    axes[0, 1].set_ylabel('Residuals ($)')
    axes[0, 1].set_title('Residual Plot')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Residuals distribution
    axes[1, 0].hist(residuals, bins=50, color='purple', edgecolor='black', alpha=0.7)
    axes[1, 0].set_xlabel('Residuals ($)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Distribution of Residuals')
    axes[1, 0].axvline(x=0, color='r', linestyle='--', lw=2)
    
    # 4. Feature importance
    features = list(feature_importance.keys())
    coefficients = list(feature_importance.values())
    colors = ['red' if c < 0 else 'green' for c in coefficients]
    axes[1, 1].barh(features, coefficients, color=colors, alpha=0.7)
    axes[1, 1].set_xlabel('Coefficient Value')
    axes[1, 1].set_title('Feature Coefficients')
    axes[1, 1].axvline(x=0, color='black', linestyle='-', lw=1)
    
    plt.tight_layout()
    plt.savefig('models/model_performance.png', dpi=300, bbox_inches='tight')
    print("\n6. Performance plots saved to 'models/model_performance.png'")
    
    # Save model
    print("\n7. Saving model...")
    model.save()
    
    # Save metrics
    metrics_df = pd.DataFrame({
        'Metric': ['R² Score', 'RMSE', 'MAE', 'MSE'],
        'Train': [train_metrics['R2'], train_metrics['RMSE'], train_metrics['MAE'], train_metrics['MSE']],
        'Test': [test_metrics['R2'], test_metrics['RMSE'], test_metrics['MAE'], test_metrics['MSE']]
    })
    metrics_df.to_csv('models/metrics.csv', index=False)
    print("   Metrics saved to 'models/metrics.csv'")
    
    print("\n" + "=" * 60)
    print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
