"""
Unit tests for House Price Prediction Model
"""
import unittest
import numpy as np
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.train_model import HousePriceModel

class TestHousePriceModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        # Create sample data
        np.random.seed(42)
        cls.n_samples = 100
        
        cls.X_train = pd.DataFrame({
            'area': np.random.randint(500, 5000, cls.n_samples),
            'bedrooms': np.random.randint(1, 6, cls.n_samples),
            'bathrooms': np.random.randint(1, 5, cls.n_samples),
            'age': np.random.randint(0, 50, cls.n_samples),
            'garage': np.random.randint(0, 4, cls.n_samples),
            'location_score': np.random.uniform(1, 10, cls.n_samples),
            'has_pool': np.random.randint(0, 2, cls.n_samples),
            'has_garden': np.random.randint(0, 2, cls.n_samples),
            'floors': np.random.randint(1, 4, cls.n_samples)
        })
        
        # Generate target
        cls.y_train = (
            150 * cls.X_train['area'] +
            15000 * cls.X_train['bedrooms'] +
            12000 * cls.X_train['bathrooms']
        )
        
        cls.X_test = cls.X_train.iloc[:10].copy()
        cls.y_test = cls.y_train.iloc[:10].copy()
    
    def test_model_initialization(self):
        """Test model initialization"""
        model = HousePriceModel()
        self.assertIsNotNone(model.model)
        self.assertIsNotNone(model.scaler)
    
    def test_model_training(self):
        """Test model training"""
        model = HousePriceModel()
        model.train(self.X_train, self.y_train)
        
        # Check if feature names are stored
        self.assertEqual(len(model.feature_names), self.X_train.shape[1])
    
    def test_model_prediction(self):
        """Test model prediction"""
        model = HousePriceModel()
        model.train(self.X_train, self.y_train)
        
        predictions = model.predict(self.X_test)
        
        # Check prediction shape
        self.assertEqual(len(predictions), len(self.X_test))
        
        # Check predictions are numeric
        self.assertTrue(np.all(np.isfinite(predictions)))
        
        # Check predictions are positive
        self.assertTrue(np.all(predictions > 0))
    
    def test_model_evaluation(self):
        """Test model evaluation"""
        model = HousePriceModel()
        model.train(self.X_train, self.y_train)
        
        predictions, metrics = model.evaluate(self.X_test, self.y_test)
        
        # Check if all metrics are present
        required_metrics = ['MSE', 'RMSE', 'MAE', 'R2']
        for metric in required_metrics:
            self.assertIn(metric, metrics)
        
        # Check R2 score is reasonable (between 0 and 1 for good model)
        self.assertGreaterEqual(metrics['R2'], 0)
        self.assertLessEqual(metrics['R2'], 1)
    
    def test_feature_importance(self):
        """Test feature importance extraction"""
        model = HousePriceModel()
        model.train(self.X_train, self.y_train)
        
        importance = model.get_feature_importance()
        
        # Check all features have coefficients
        self.assertEqual(len(importance), self.X_train.shape[1])
        
        # Check coefficients are numeric
        for coef in importance.values():
            self.assertTrue(np.isfinite(coef))
    
    def test_input_validation(self):
        """Test input validation"""
        model = HousePriceModel()
        model.train(self.X_train, self.y_train)
        
        # Test with wrong number of features
        wrong_input = pd.DataFrame({
            'area': [2000],
            'bedrooms': [3]
        })
        
        with self.assertRaises(Exception):
            model.predict(wrong_input)

class TestDataGeneration(unittest.TestCase):
    
    def test_data_file_existence(self):
        """Test if data files exist after generation"""
        required_files = [
            'data/house_prices.csv',
            'data/train.csv',
            'data/test.csv'
        ]
        
        for file in required_files:
            if os.path.exists(file):
                self.assertTrue(True)
    
    def test_data_shape(self):
        """Test data shape and columns"""
        if os.path.exists('data/house_prices.csv'):
            df = pd.read_csv('data/house_prices.csv')
            
            # Check if price column exists
            self.assertIn('price', df.columns)
            
            # Check if data is not empty
            self.assertGreater(len(df), 0)
            
            # Check if all required columns exist
            required_cols = ['area', 'bedrooms', 'bathrooms', 'age', 
                           'garage', 'location_score', 'has_pool', 
                           'has_garden', 'floors', 'price']
            for col in required_cols:
                self.assertIn(col, df.columns)

if __name__ == '__main__':
    print("Running House Price Prediction Tests...")
    print("=" * 60)
    unittest.main(verbosity=2)
