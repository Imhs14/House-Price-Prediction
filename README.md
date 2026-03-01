# 🏠 House Price Prediction System

A complete end-to-end machine learning project for predicting house prices using Linear Regression, with a beautiful Streamlit web interface for deployment.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Results](#results)
- [Technologies Used](#technologies-used)

## 🎯 Overview

This project demonstrates a complete machine learning pipeline from data generation to model deployment. It predicts house prices based on features like square footage, number of bedrooms/bathrooms, age, garage spaces, lot size, and neighborhood quality.

## ✨ Features

- **Data Generation**: Synthetic dataset with realistic house features
- **Data Preprocessing**: Feature scaling and train-test split
- **Model Training**: Linear Regression with performance evaluation
- **Visualizations**: 
  - Correlation matrix
  - Feature distributions
  - Prediction plots
  - Feature importance
- **Interactive Web App**: Streamlit interface for real-time predictions
- **Model Persistence**: Save and load trained models
- **Performance Metrics**: R², RMSE, MAE, MSE

## 📁 Project Structure

```
house_price_prediction/
│
├── data/                          # Data directory
│   └── house_prices.csv          # Generated dataset
│
├── models/                        # Saved models
│   ├── house_price_model.pkl     # Trained model
│   ├── scaler.pkl                # Feature scaler
│   └── metrics.json              # Model metrics
│
├── notebooks/                     # Visualizations
│   ├── correlation_matrix.png
│   ├── feature_distributions.png
│   ├── predictions_plot.png
│   └── feature_importance.png
│
├── src/                           # Source code
│   ├── preprocessing.py          # Data preprocessing
│   ├── model.py                  # Model training & evaluation
│   └── visualization.py          # Plotting functions
│
├── generate_data.py              # Data generation script
├── train.py                      # Main training pipeline
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download the Project

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

### 1. Generate Dataset

```bash
python generate_data.py
```

This creates a synthetic dataset with 1000 house records in `data/house_prices.csv`.

### 2. Train the Model

```bash
python train.py
```

This script will:
- Load and preprocess the data
- Create visualizations
- Train the Linear Regression model
- Evaluate performance
- Save the model and metrics

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

The web application will open in your browser (usually at `http://localhost:8501`).

## 🤖 Model Details

### Algorithm
**Linear Regression** - A simple yet effective algorithm that models the relationship between features and target variable using a linear equation.

### Input Features
1. **square_feet** - Total living area (800-5000 sq ft)
2. **bedrooms** - Number of bedrooms (1-7)
3. **bathrooms** - Number of bathrooms (1-5)
4. **age** - Age of house in years (0-100)
5. **garage_spaces** - Number of garage spaces (0-4)
6. **lot_size** - Property size (2000-20000 sq ft)
7. **neighborhood_score** - Neighborhood quality (1-10)

### Target Variable
**price** - House price in USD

### Preprocessing
- **Train-Test Split**: 80-20 split
- **Feature Scaling**: StandardScaler for normalization

## 📊 Results

The model achieves strong performance on the synthetic dataset:

- **R² Score**: ~0.99 (explains 99% of variance)
- **RMSE**: ~$30,000
- **MAE**: ~$24,000

*Note: These metrics are based on synthetic data. Real-world performance may vary.*

## 🛠️ Technologies Used

### Machine Learning & Data Science
- **Scikit-learn**: Model training and evaluation
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations

### Visualization
- **Matplotlib**: Static plots
- **Seaborn**: Statistical visualizations
- **Plotly**: Interactive charts

### Web Application
- **Streamlit**: Web interface framework

### Model Persistence
- **Joblib**: Model serialization

## 📈 Key Insights

Based on the Linear Regression coefficients:
- **Square footage** has the strongest positive impact on price
- **Neighborhood score** significantly affects house value
- **Age** negatively impacts price (depreciation)
- **Bedrooms and bathrooms** add substantial value
- **Garage spaces** and **lot size** contribute moderately

## 🔮 Future Enhancements

- Add more advanced algorithms (Random Forest, XGBoost)
- Implement feature engineering
- Add real-world dataset option
- Include model comparison dashboard
- Add data upload functionality
- Implement model retraining pipeline
- Add price trend analysis over time

## 📝 Notes

- This is a demonstration project using synthetic data
- The dataset is randomly generated with realistic relationships
- Not intended for actual real estate price predictions
- Best used for learning ML pipeline development

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Predicting! 🏡💰**
