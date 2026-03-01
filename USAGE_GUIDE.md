# 🚀 Usage Guide - House Price Prediction System

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate Data and Train Model
```bash
# Generate the dataset
python generate_data.py

# Train the model
python train.py
```

### Step 3: Launch the Web App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📖 Detailed Instructions

### 1. Environment Setup

#### Option A: Using pip
```bash
pip install -r requirements.txt
```

#### Option B: Using virtual environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate Dataset

Run the data generation script:
```bash
python generate_data.py
```

This will:
- Create a synthetic dataset with 1000 house records
- Save it to `data/house_prices.csv`
- Display dataset statistics

**Output:**
```
Dataset created with 1000 samples
Dataset shape: (1000, 8)
```

### 3. Train the Model

Run the training pipeline:
```bash
python train.py
```

This comprehensive pipeline will:
1. Load and preprocess the data
2. Create visualizations (correlation matrix, distributions)
3. Split data into train/test sets (80/20)
4. Scale features using StandardScaler
5. Train Linear Regression model
6. Evaluate model performance
7. Generate prediction plots
8. Save model, scaler, and metrics

**Expected Output:**
```
============================================================
HOUSE PRICE PREDICTION - TRAINING PIPELINE
============================================================

Model Performance Summary:
  - R² Score: ~0.97-0.98
  - RMSE: ~$29,000-$30,000
  - MAE: ~$22,000-$24,000
```

**Files Created:**
- `models/house_price_model.pkl` - Trained model
- `models/scaler.pkl` - Feature scaler
- `models/metrics.json` - Performance metrics
- `notebooks/correlation_matrix.png` - Feature correlations
- `notebooks/feature_distributions.png` - Feature distributions
- `notebooks/predictions_plot.png` - Actual vs Predicted
- `notebooks/feature_importance.png` - Feature coefficients

### 4. Launch Streamlit App

Start the web application:
```bash
streamlit run app.py
```

**Features:**
- 🔮 **Prediction Tab**: Make real-time price predictions
- 📊 **Model Performance Tab**: View model metrics
- ℹ️ **About Tab**: Learn about the system

### 5. Using the Web App

#### Making Predictions:

1. **Navigate to the "Prediction" tab**
2. **Enter house features:**
   - Square Feet (500-10,000)
   - Number of Bedrooms (1-10)
   - Number of Bathrooms (1-8)
   - Age of House (0-200 years)
   - Garage Spaces (0-5)
   - Lot Size (1,000-50,000 sq ft)
   - Neighborhood Score (1.0-10.0)

3. **Click "Predict House Price"**
4. **View results:**
   - Predicted price
   - Input summary
   - Price range estimate (±10%)

#### Example Input:
```
Square Feet: 2500
Bedrooms: 4
Bathrooms: 3
Age: 5 years
Garage Spaces: 2
Lot Size: 8000 sq ft
Neighborhood Score: 7.5
```

#### Example Output:
```
Predicted Price: $748,523.45
Price Range: $673,671 - $823,376
```

---

## 🔧 Advanced Usage

### Custom Dataset

To use your own dataset:

1. **Prepare CSV with these columns:**
   - square_feet
   - bedrooms
   - bathrooms
   - age
   - garage_spaces
   - lot_size
   - neighborhood_score
   - price (target variable)

2. **Place CSV in `data/` directory**

3. **Update data path in `train.py`:**
```python
preprocessor = DataPreprocessor('data/your_dataset.csv')
```

4. **Run training:**
```bash
python train.py
```

### Retraining the Model

To retrain with new data:

```bash
# Generate new dataset
python generate_data.py

# Retrain model
python train.py

# Restart Streamlit app
streamlit run app.py
```

### Using the Model Programmatically

```python
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load('models/house_price_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Prepare input
input_data = pd.DataFrame({
    'square_feet': [2500],
    'bedrooms': [4],
    'bathrooms': [3],
    'age': [5],
    'garage_spaces': [2],
    'lot_size': [8000],
    'neighborhood_score': [7.5]
})

# Scale and predict
input_scaled = scaler.transform(input_data)
prediction = model.predict(input_scaled)[0]

print(f"Predicted Price: ${prediction:,.2f}")
```

---

## 📊 Understanding the Results

### Model Metrics

**R² Score (0.97-0.98)**
- Excellent! Model explains 97-98% of price variance
- Closer to 1.0 is better
- Above 0.7 is considered good

**RMSE ($29,000-$30,000)**
- Average prediction error
- Model predictions typically within $30k of actual price
- Lower is better

**MAE ($22,000-$24,000)**
- Average absolute error
- More interpretable than RMSE
- 50% of predictions are within this range

### Feature Importance

Based on coefficient values:

1. **Square Feet** (~180,000) - Most important
2. **Neighborhood Score** (~51,000)
3. **Lot Size** (~26,000)
4. **Bedrooms** (~25,000)
5. **Bathrooms** (~10,000)
6. **Garage Spaces** (~8,000)
7. **Age** (~-15,000) - Negative impact

**Interpretation:**
- Each additional square foot adds ~$180 to price
- Each point in neighborhood score adds ~$51,000
- Each year of age reduces price by ~$15,000

---

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: File not found errors

**Solution:**
```bash
# Ensure you're in the project directory
cd house_price_prediction

# Create directories
mkdir -p data models notebooks

# Run scripts
python generate_data.py
python train.py
```

### Issue: Streamlit won't start

**Solution:**
```bash
# Check if model files exist
ls models/

# If missing, train the model first
python train.py

# Then run Streamlit
streamlit run app.py
```

### Issue: Port already in use

**Solution:**
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

---

## 🎯 Tips for Best Results

1. **Feature Values**: Use realistic values for better predictions
2. **Neighborhood Score**: Has significant impact (1-10 scale)
3. **Square Feet**: Most influential feature
4. **Age**: Older houses generally valued lower
5. **Consistency**: Keep feature relationships logical

---

## 📞 Support

For issues or questions:
1. Check the README.md file
2. Review the code comments
3. Examine the training logs
4. Verify all dependencies are installed

---

## 🎓 Learning Resources

### Understanding Linear Regression
- Simple, interpretable algorithm
- Models linear relationships
- Coefficients show feature impact
- Fast training and prediction

### Key Concepts
- **Feature Scaling**: Normalizes feature ranges
- **Train-Test Split**: Validates model generalization
- **R² Score**: Measures prediction accuracy
- **Residuals**: Prediction errors

---

**Happy Learning! 🚀**
