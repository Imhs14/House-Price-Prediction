import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import os

# 1. Load the real Kaggle Data
# Ensure train.csv is placed in a 'data' folder in your root directory
data = pd.read_csv('data/train.csv')

# 2. Select Features mapping to your requirements
# Size = GrLivArea, Rooms = BedroomAbvGr/FullBath, Location = Neighborhood
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath', 'Neighborhood', 'OverallQual', 'YearBuilt']
target = 'SalePrice'

X = data[features]
y = data[target]

# 3. Preprocessing Setup
numeric_features = ['GrLivArea', 'BedroomAbvGr', 'FullBath', 'OverallQual', 'YearBuilt']
categorical_features = ['Neighborhood']

# Handle missing numbers with the median, then scale them
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Handle missing categories with the most frequent, then One-Hot Encode them
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine both preprocessors
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 4. Create the final ML Pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 5. Train-Test Split (80-20 split as per your original design)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train the Model
print("Training Linear Regression model on Kaggle data...")
model_pipeline.fit(X_train, y_train)

# 7. Evaluate the Model
y_pred = model_pipeline.predict(X_test)
print("\n--- Model Evaluation ---")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: ${np.sqrt(mean_squared_error(y_test, y_pred)):,.2f}")
print(f"MAE: ${mean_absolute_error(y_test, y_pred):,.2f}")

# 8. Save the Pipeline
os.makedirs('model', exist_ok=True)
joblib.dump(model_pipeline, 'model/house_price_model.pkl')
print("\nModel pipeline saved successfully to model/house_price_model.pkl")