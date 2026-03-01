"""
Main training pipeline
"""
import sys
import os

# Add src directory to path
sys.path.append('src')

from preprocessing import DataPreprocessor
from model import HousePriceModel
from visualization import Visualizer

def main():
    """Execute the complete training pipeline"""
    
    print("=" * 60)
    print("HOUSE PRICE PREDICTION - TRAINING PIPELINE")
    print("=" * 60)
    
    # Step 1: Data Loading and Preprocessing
    print("\n[STEP 1] Loading and Preprocessing Data...")
    preprocessor = DataPreprocessor('data/house_prices.csv')
    df = preprocessor.load_data()
    
    # Display basic info
    print(f"\nDataset Info:")
    print(df.info())
    print(f"\nDataset Statistics:")
    print(df.describe())
    
    # Step 2: Visualize data
    print("\n[STEP 2] Creating Visualizations...")
    visualizer = Visualizer()
    visualizer.plot_correlation_matrix(df)
    visualizer.plot_feature_distributions(df)
    
    # Step 3: Prepare features and target
    print("\n[STEP 3] Preparing Features and Target...")
    X, y = preprocessor.get_features_target(df)
    print(f"Features: {list(X.columns)}")
    print(f"Target: price")
    
    # Step 4: Split data
    print("\n[STEP 4] Splitting Data...")
    X_train, X_test, y_train, y_test = preprocessor.split_data(X, y)
    
    # Step 5: Scale features
    print("\n[STEP 5] Scaling Features...")
    X_train_scaled, X_test_scaled = preprocessor.scale_features(X_train, X_test)
    preprocessor.save_scaler()
    
    # Step 6: Train model
    print("\n[STEP 6] Training Linear Regression Model...")
    model = HousePriceModel()
    model.train(X_train_scaled, y_train)
    
    # Step 7: Evaluate model
    print("\n[STEP 7] Evaluating Model...")
    metrics = model.evaluate(X_test_scaled, y_test)
    
    # Step 8: Feature importance
    print("\n[STEP 8] Analyzing Feature Importance...")
    feature_importance = model.get_feature_importance(preprocessor.feature_names)
    print("\nFeature Coefficients:")
    print(feature_importance)
    
    # Step 9: Visualize predictions
    print("\n[STEP 9] Visualizing Predictions...")
    y_pred = model.predict(X_test_scaled)
    visualizer.plot_predictions(y_test, y_pred)
    visualizer.plot_feature_importance(feature_importance)
    
    # Step 10: Save model and metrics
    print("\n[STEP 10] Saving Model and Metrics...")
    model.save_model()
    model.save_metrics()
    
    print("\n" + "=" * 60)
    print("TRAINING PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nModel Performance Summary:")
    print(f"  - R² Score: {metrics['r2_score']:.4f}")
    print(f"  - RMSE: ${metrics['rmse']:,.2f}")
    print(f"  - MAE: ${metrics['mae']:,.2f}")
    print(f"\nFiles saved:")
    print(f"  - Model: models/house_price_model.pkl")
    print(f"  - Scaler: models/scaler.pkl")
    print(f"  - Metrics: models/metrics.json")
    print(f"  - Visualizations: notebooks/")

if __name__ == "__main__":
    main()
