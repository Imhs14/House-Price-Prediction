# 🏗️ Project Architecture

## Overview

This document explains the architecture and design decisions of the House Price Prediction System.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACE                          │
│                   (Streamlit Web App)                       │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  Prediction  │  │ Performance  │  │    About     │    │
│  │     Tab      │  │     Tab      │  │     Tab      │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    MODEL LAYER                              │
│                                                             │
│  ┌─────────────────┐        ┌──────────────────┐          │
│  │ Trained Model   │◄───────┤  Feature Scaler  │          │
│  │ (Linear Reg)    │        │ (StandardScaler) │          │
│  └─────────────────┘        └──────────────────┘          │
│           │                           │                     │
│           └───────────┬───────────────┘                     │
│                       │                                      │
│                  Predictions                                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                 PROCESSING LAYER                            │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │     Data     │  │    Model     │  │Visualization │    │
│  │Preprocessing │  │   Training   │  │   Engine     │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     DATA LAYER                              │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Raw Data   │  │   Models     │  │Visualizations│    │
│  │    (CSV)     │  │    (PKL)     │  │    (PNG)     │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Data Layer

#### Purpose
Store and manage all data assets including raw data, trained models, and visualizations.

#### Components
- **Raw Data** (`data/house_prices.csv`)
  - Synthetic dataset with 1000 samples
  - 7 input features + 1 target variable
  - Generated with realistic relationships

- **Model Files** (`models/`)
  - `house_price_model.pkl`: Trained Linear Regression model
  - `scaler.pkl`: StandardScaler for feature normalization
  - `metrics.json`: Performance metrics

- **Visualizations** (`notebooks/`)
  - Correlation matrices
  - Feature distributions
  - Prediction plots
  - Feature importance charts

### 2. Processing Layer

#### DataPreprocessor (`src/preprocessing.py`)
**Responsibilities:**
- Load data from CSV
- Separate features and target
- Train-test split (80/20)
- Feature scaling with StandardScaler
- Save/load scaler

**Key Methods:**
```python
load_data() -> DataFrame
get_features_target(df) -> (X, y)
split_data(X, y) -> (X_train, X_test, y_train, y_test)
scale_features(X_train, X_test) -> (X_train_scaled, X_test_scaled)
```

#### HousePriceModel (`src/model.py`)
**Responsibilities:**
- Train Linear Regression model
- Make predictions
- Evaluate performance (MSE, RMSE, MAE, R²)
- Calculate feature importance
- Save/load model

**Key Methods:**
```python
train(X_train, y_train)
predict(X) -> predictions
evaluate(X_test, y_test) -> metrics
get_feature_importance(feature_names) -> coefficients
```

#### Visualizer (`src/visualization.py`)
**Responsibilities:**
- Create correlation matrices
- Plot feature distributions
- Visualize predictions vs actual
- Display feature importance
- Generate professional plots

**Key Methods:**
```python
plot_correlation_matrix(df)
plot_feature_distributions(df)
plot_predictions(y_true, y_pred)
plot_feature_importance(coefficients)
```

### 3. Model Layer

#### Linear Regression Model
**Algorithm:** Ordinary Least Squares (OLS)
**Equation:** `y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε`

**Characteristics:**
- Fast training and inference
- Highly interpretable coefficients
- Assumes linear relationships
- No hyperparameters to tune

**Performance:**
- R² Score: ~0.97-0.98 (Excellent)
- RMSE: ~$29,000-$30,000
- MAE: ~$22,000-$24,000

### 4. User Interface

#### Streamlit Web App (`app.py`)
**Pages:**

1. **Prediction Tab**
   - Interactive input fields
   - Real-time predictions
   - Price range estimates
   - Input summary
   - Gauge charts

2. **Performance Tab**
   - Model metrics display
   - R² Score gauge
   - Error metrics
   - Metric explanations

3. **About Tab**
   - System documentation
   - Feature descriptions
   - Technology stack
   - How it works

**Features:**
- Responsive design
- Custom styling
- Interactive Plotly charts
- Real-time updates
- Model caching for performance

## Data Flow

### Training Pipeline
```
1. generate_data.py
   └─> Creates synthetic dataset
       └─> data/house_prices.csv

2. train.py
   └─> Loads data
       └─> Preprocesses features
           └─> Trains model
               └─> Evaluates performance
                   └─> Saves artifacts
                       ├─> models/house_price_model.pkl
                       ├─> models/scaler.pkl
                       ├─> models/metrics.json
                       └─> notebooks/*.png
```

### Prediction Pipeline
```
1. User inputs features
   └─> app.py receives input

2. Input validation
   └─> Convert to DataFrame

3. Feature scaling
   └─> scaler.transform(input)

4. Model prediction
   └─> model.predict(input_scaled)

5. Display results
   └─> Show price + visualizations
```

## Design Patterns

### 1. Separation of Concerns
- Data preprocessing separate from modeling
- Visualization separate from business logic
- UI separate from model logic

### 2. Modularity
- Each component is independently testable
- Easy to swap implementations
- Clear interfaces between modules

### 3. Single Responsibility
- Each class has one primary purpose
- Methods perform specific tasks
- Easy to understand and maintain

### 4. DRY (Don't Repeat Yourself)
- Reusable utility functions
- Centralized configuration
- Shared constants

## Technology Stack Justification

### Why Linear Regression?
- **Interpretability**: Coefficients show exact impact
- **Simplicity**: Easy to understand and explain
- **Speed**: Fast training and inference
- **Baseline**: Good starting point for comparison

### Why Streamlit?
- **Rapid Development**: Quick prototyping
- **Python Native**: No separate frontend language
- **Interactive**: Built-in widgets and charts
- **Deployment**: Easy cloud deployment

### Why StandardScaler?
- **Normalization**: Puts features on same scale
- **Improved Performance**: Helps with convergence
- **Required**: Important for distance-based algorithms
- **Interpretability**: Maintains coefficient meaning

### Why Joblib for Model Persistence?
- **Efficiency**: Optimized for large numpy arrays
- **Compression**: Smaller file sizes
- **Speed**: Fast serialization/deserialization
- **Standard**: Scikit-learn recommended

## Security Considerations

### Input Validation
- Min/max constraints on all inputs
- Type checking for numeric values
- Range validation for scores

### Model Security
- Model files stored securely
- No user access to model internals
- Prediction-only interface

### Data Privacy
- No personal data collected
- No data persistence in app
- Synthetic dataset only

## Scalability Considerations

### Current Limitations
- Single-user deployment
- Local model loading
- In-memory processing
- No database integration

### Future Improvements
- Multi-user support with session management
- Cloud model hosting (AWS S3, GCS)
- Database for data persistence
- Containerization with Docker
- CI/CD pipeline
- Model versioning
- A/B testing framework

## Performance Optimization

### Current Optimizations
- Model caching with `@st.cache_resource`
- Efficient numpy operations
- Minimal data loading
- Optimized visualizations

### Potential Improvements
- Batch prediction support
- Async model loading
- Redis caching layer
- Model quantization
- GPU acceleration for large datasets

## Error Handling

### Training Pipeline
- File existence checks
- Data validation
- Graceful failures with informative messages
- Automatic directory creation

### Web Application
- Missing model file detection
- Input validation with user feedback
- Try-catch blocks for predictions
- Fallback displays for errors

## Testing Strategy

### Unit Tests (Future)
```python
test_preprocessing.py
test_model.py
test_visualization.py
test_app.py
```

### Integration Tests (Future)
```python
test_training_pipeline.py
test_prediction_pipeline.py
```

### Manual Testing
- Input validation with edge cases
- Prediction accuracy verification
- UI responsiveness testing
- Cross-browser compatibility

## Deployment Options

### Local Deployment
```bash
streamlit run app.py
```

### Cloud Deployment

**Streamlit Cloud:**
```bash
# Connect GitHub repo
# Deploy with one click
```

**Heroku:**
```bash
# Add Procfile
web: streamlit run app.py
```

**AWS EC2:**
```bash
# Install dependencies
# Run with systemd service
```

**Docker:**
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD streamlit run app.py
```

## Monitoring and Logging

### Current Logging
- Print statements for training progress
- Error messages for failures
- Success confirmations

### Future Enhancements
- Structured logging with Python logging module
- Performance metrics tracking
- User interaction analytics
- Model performance monitoring
- Prediction distribution tracking

## Maintenance

### Regular Tasks
- Retrain model with new data
- Update dependencies
- Review and optimize performance
- User feedback incorporation

### Model Updates
1. Generate new dataset or use real data
2. Run training pipeline
3. Evaluate performance
4. Compare with previous version
5. Deploy if improved

## Conclusion

This architecture provides a solid foundation for a machine learning prediction system with clear separation of concerns, maintainable code, and room for future enhancements. The modular design allows for easy testing, debugging, and extension of functionality.
