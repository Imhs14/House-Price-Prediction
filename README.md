# 🏠 House Price Prediction System

A complete end-to-end machine learning project for predicting house prices using Linear Regression on the real-world **Kaggle Ames Housing Dataset**, complete with a beautiful Streamlit web interface for deployment.

## 📋 Table of Contents

* [Overview](https://www.google.com/search?q=%23overview)
* [Features](https://www.google.com/search?q=%23features)
* [Project Structure](https://www.google.com/search?q=%23project-structure)
* [Installation](https://www.google.com/search?q=%23installation)
* [Usage](https://www.google.com/search?q=%23usage)
* [Model Details](https://www.google.com/search?q=%23model-details)
* [Results](https://www.google.com/search?q=%23results)
* [Technologies Used](https://www.google.com/search?q=%23technologies-used)

## 🎯 Overview

This project demonstrates a professional machine learning pipeline. It predicts house prices based on real-world features like above-ground living area, bedrooms, bathrooms, year built, overall material quality, and specific neighborhoods in Ames, Iowa.

## ✨ Features

* **Real-World Data**: Utilizes the industry-standard Kaggle Ames Housing Dataset.
* **Robust Preprocessing Pipeline**: Implements `scikit-learn` Pipelines with `SimpleImputer`, `StandardScaler`, and `OneHotEncoder` to handle missing values and categorical data automatically.
* **Model Training**: Linear Regression with strict training/testing splits to prevent data leakage.
* **Visualizations**:
* Correlation matrix
* Feature distributions
* Prediction plots
* Feature importance


* **Interactive Web App**: Streamlit interface with dynamic dropdowns and real-time predictions.
* **Model Persistence**: Save and load the entire trained pipeline using Joblib.
* **Performance Metrics**: R², RMSE, MAE, MSE.

## 📁 Project Structure

```text
house_price_prediction/
│
├── data/                          # Data directory
│   └── train.csv                 # Kaggle Ames Housing Dataset
│
├── models/                        # Saved models
│   ├── house_price_model.pkl     # Trained ML Pipeline (Imputer + Scaler + Encoder + Model)
│   └── metrics.json              # Model metrics
│
├── notebooks/                     # Visualizations
│   ├── correlation_matrix.png
│   ├── feature_distributions.png
│   ├── predictions_plot.png
│   └── feature_importance.png
│
├── src/                           # Source code
│   ├── preprocessing.py          # Data preprocessing components
│   ├── model.py                  # Model training & evaluation
│   └── visualization.py          # Plotting functions
│
├── train_model.py                # Main training pipeline script
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
└── README.md                     # This file

```

## 🚀 Installation

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/Imhs14/House-Price-Prediction.git
cd House-Price-Prediction

```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt

```

### Step 3: Download the Dataset

Download `train.csv` from the [Kaggle House Prices Competition](https://www.google.com/search?q=https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) and place it inside the `data/` folder.

## 💻 Usage

### 1. Train the Model

```bash
python train_model.py

```

This script will:

* Load the Kaggle dataset.
* Build and fit the preprocessing pipeline (imputation, scaling, encoding).
* Train the Linear Regression model.
* Evaluate performance on unseen test data.
* Save the entire pipeline and metrics.

### 2. Run the Streamlit App

```bash
streamlit run app.py

```

The web application will open in your browser (usually at `http://localhost:8501`).

## 🤖 Model Details

### Algorithm

**Linear Regression** - Mapped through a `scikit-learn` Pipeline to seamlessly handle raw input data directly from the user interface.

### Input Features

1. **GrLivArea** - Above grade (ground) living area square feet
2. **BedroomAbvGr** - Number of bedrooms above basement level
3. **FullBath** - Full bathrooms above grade
4. **YearBuilt** - Original construction date
5. **OverallQual** - Overall material and finish quality (1-10)
6. **Neighborhood** - Physical locations within Ames city limits (Categorical)

### Target Variable

**SalePrice** - Property sale price in USD

### Preprocessing Pipeline

* **Missing Numeric Data**: Imputed using the median strategy.
* **Missing Categorical Data**: Imputed using the most frequent strategy.
* **Numeric Scaling**: `StandardScaler` for normalization.
* **Categorical Encoding**: `OneHotEncoder` to translate text-based neighborhoods into machine-readable formats.
* **Train-Test Split**: 80-20 split.

## 📊 Results

The model achieves realistic and strong performance on real-world housing data:

* **R² Score**: ~0.85 (explains 85% of variance in real-world prices)
* **RMSE**: ~$35,000
* **MAE**: ~$25,000

*Note: These metrics reflect the natural noise and variance found in actual real estate markets, avoiding the overfitting commonly seen with synthetic datasets.*

## 🛠️ Technologies Used

### Machine Learning & Data Science

* **Scikit-learn**: Pipelines, Transformers, and Linear Regression
* **Pandas**: Data manipulation and ingestion
* **NumPy**: Numerical operations

### Visualization

* **Plotly**: Interactive charts and gauges
* **Matplotlib / Seaborn**: Statistical visualizations

### Web Application

* **Streamlit**: Web interface framework

### Model Persistence

* **Joblib**: Pipeline serialization

## 📈 Key Insights

Based on real-world data analysis:

* **Overall Quality** and **Living Area** are the strongest predictors of sale price.
* **Neighborhood** plays a massive role in valuation, requiring categorical encoding to capture properly.
* **Age (Year Built)** shows a clear depreciation curve for older homes that haven't been remodeled.

## 🔮 Future Enhancements

* Add more advanced algorithms (Random Forest, XGBoost) to capture non-linear relationships.
* Expand the feature selection to include basement square footage and garage condition.
* Implement an automated hyperparameter tuning grid.
* Add data upload functionality for bulk predictions.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Predicting! 🏡💰***
