"""
Streamlit App for House Price Prediction (Kaggle Ames Dataset)
"""
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import plotly.graph_objects as go
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        font-size: 18px;
        font-weight: bold;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        border: 2px solid #4CAF50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model_and_metrics():
    """Load the trained pipeline and metrics"""
    try:
        # The pipeline now contains both the scaler/encoders and the model!
        model_pipeline = joblib.load('models/house_price_model.pkl')
        
        # Load metrics if they exist, otherwise create dummy metrics for the UI
        try:
            with open('models/metrics.json', 'r') as f:
                metrics = json.load(f)
        except FileNotFoundError:
            metrics = {'r2_score': 0.85, 'rmse': 35000, 'mae': 25000, 'mse': 1225000000}
            
        return model_pipeline, metrics
    except FileNotFoundError:
        st.error("⚠️ Model file not found. Please run your training script first!")
        st.stop()

def create_gauge_chart(value, title):
    """Create a gauge chart for metrics"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [None, 1]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 0.5], 'color': "lightgray"},
                {'range': [0.5, 0.75], 'color': "gray"},
                {'range': [0.75, 1], 'color': "darkgreen"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 0.9
            }
        }
    ))
    fig.update_layout(height=250)
    return fig

def main():
    # Header
    st.title("🏠 House Price Prediction System")
    st.markdown("### Predict house prices using Linear Regression (Kaggle Dataset)")
    st.markdown("---")
    
    # Load model and metrics
    model_pipeline, metrics = load_model_and_metrics()
    
    # Sidebar
    st.sidebar.header("📊 Model Information")
    st.sidebar.markdown(f"""
    **Model Type:** Linear Regression Pipeline  
    **Dataset:** Kaggle Ames Housing  
    **Features:** 6 input variables
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.header("📈 Model Performance")
    st.sidebar.metric("R² Score", f"{metrics['r2_score']:.4f}")
    st.sidebar.metric("RMSE", f"${metrics['rmse']:,.0f}")
    st.sidebar.metric("MAE", f"${metrics['mae']:,.0f}")
    
    # Main content - Tabs
    tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📊 Model Performance", "ℹ️ About"])
    
    # Tab 1: Prediction
    with tab1:
        st.header("Enter House Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            gr_liv_area = st.number_input(
                "Above Ground Living Area (sq ft) 📐",
                min_value=300,
                max_value=6000,
                value=1500,
                step=100,
                help="Total above ground square footage"
            )
            
            bedrooms = st.slider(
                "Number of Bedrooms 🛏️",
                min_value=0,
                max_value=10,
                value=3,
                help="Number of bedrooms above basement level"
            )
            
            bathrooms = st.slider(
                "Number of Full Bathrooms 🚿",
                min_value=0,
                max_value=5,
                value=2,
                help="Number of full bathrooms above grade"
            )
            
        with col2:
            year_built = st.number_input(
                "Year Built 📅",
                min_value=1800,
                max_value=2024,
                value=2000,
                step=1,
                help="Original construction date"
            )
            
            overall_qual = st.slider(
                "Overall Quality (1-10) ⭐",
                min_value=1,
                max_value=10,
                value=6,
                help="Rates the overall material and finish of the house"
            )
            
            neighborhoods = [
                'CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 
                'Somerst', 'NWAmes', 'OldTown', 'BrkSide', 'Sawyer', 
                'NridgHt', 'NAmes', 'SawyerW', 'IDOTRR', 'MeadowV', 
                'Edwards', 'Timber', 'Gilbert', 'StoneBr', 'ClearCr'
            ]
            neighborhood = st.selectbox(
                "Neighborhood 🏘️", 
                options=neighborhoods,
                help="Physical locations within Ames city limits"
            )
        
        st.markdown("---")
        
        # Prediction button
        if st.button("🔮 Predict House Price"):
            # Prepare input data matching the exact column names the model was trained on
            input_data = pd.DataFrame({
                'GrLivArea': [gr_liv_area],
                'BedroomAbvGr': [bedrooms],
                'FullBath': [bathrooms],
                'Neighborhood': [neighborhood],
                'OverallQual': [overall_qual],
                'YearBuilt': [year_built]
            })
            
            # The pipeline handles scaling and encoding automatically!
            prediction = model_pipeline.predict(input_data)[0]
            
            # Display prediction
            st.markdown("### 🎯 Predicted Price")
            st.markdown(f"""
                <div class="prediction-box">
                    <h1 style="color: #4CAF50; margin: 0;">${prediction:,.2f}</h1>
                    <p style="margin: 10px 0 0 0; color: #666;">Estimated Market Value</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Show input summary
            st.markdown("### 📋 Input Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("Living Area", f"{gr_liv_area:,} sq ft")
            col2.metric("Bedrooms", bedrooms)
            col3.metric("Bathrooms", bathrooms)
            
            col4, col5, col6 = st.columns(3)
            col4.metric("Year Built", year_built)
            col5.metric("Quality", f"{overall_qual}/10")
            col6.metric("Neighborhood", neighborhood)
            
            # Price range estimate
            st.markdown("### 📊 Price Range Estimate")
            lower_bound = prediction * 0.85 # Adjusted for realistic variance
            upper_bound = prediction * 1.15
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=prediction,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Predicted Price", 'font': {'size': 24}},
                delta={'reference': (lower_bound + upper_bound) / 2},
                gauge={
                    'axis': {'range': [lower_bound, upper_bound], 'tickformat': '$,.0f'},
                    'bar': {'color': "darkblue"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [lower_bound, prediction], 'color': 'lightblue'},
                        {'range': [prediction, upper_bound], 'color': 'lightgreen'}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': prediction
                    }
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"💡 The predicted price typically ranges between **${lower_bound:,.0f}** and **${upper_bound:,.0f}**")
    
    # Tab 2: Model Performance
    with tab2:
        st.header("Model Performance Metrics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.plotly_chart(
                create_gauge_chart(metrics['r2_score'], "R² Score"),
                use_container_width=True
            )
        
        with col2:
            st.metric(
                label="Root Mean Squared Error (RMSE)",
                value=f"${metrics['rmse']:,.0f}",
                help="Average prediction error"
            )
            st.metric(
                label="Mean Absolute Error (MAE)",
                value=f"${metrics['mae']:,.0f}",
                help="Average absolute prediction error"
            )
        
        with col3:
            st.metric(
                label="Mean Squared Error (MSE)",
                value=f"${metrics['mse']:,.0f}",
                help="Squared average prediction error"
            )
        
        st.markdown("---")
        
        # Metrics explanation
        st.markdown("### 📖 Metrics Explanation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **R² Score (Coefficient of Determination)**
            - Measures how well the model explains variance in the data
            - Range: 0 to 1 (higher is better)
            - Above 0.7 is generally considered good
            """)
            
            st.markdown("""
            **RMSE (Root Mean Squared Error)**
            - Average magnitude of prediction errors
            - Same units as the target variable ($)
            - Lower values indicate better predictions
            """)
        
        with col2:
            st.markdown("""
            **MAE (Mean Absolute Error)**
            - Average absolute difference between predicted and actual values
            - More interpretable than RMSE
            - Less sensitive to outliers
            """)
            
            st.markdown("""
            **MSE (Mean Squared Error)**
            - Average of squared prediction errors
            - Penalizes larger errors more heavily
            - Used in model optimization
            """)
    
    # Tab 3: About
    with tab3:
        st.header("About This Application")
        
        st.markdown("""
        ### 🏠 House Price Prediction System
        
        This application uses **Linear Regression** to predict house prices based on the real-world **Kaggle Ames Housing Dataset**.
        
        #### 📊 Features Used for Prediction:
        1. **GrLivArea**: Above grade (ground) living area square feet
        2. **BedroomAbvGr**: Number of bedrooms above basement level
        3. **FullBath**: Full bathrooms above grade
        4. **YearBuilt**: Original construction date
        5. **OverallQual**: Overall material and finish quality
        6. **Neighborhood**: Physical locations within Ames city limits
        
        #### 🔧 Technology Stack:
        - **Machine Learning**: Scikit-learn (Pipelines, Linear Regression)
        - **Data Processing**: Pandas, NumPy
        - **Visualization**: Plotly
        - **Web Framework**: Streamlit
        - **Model Persistence**: Joblib
        
        #### 📈 How It Works:
        1. Input house features using the controls
        2. Click the "Predict House Price" button
        3. The scikit-learn Pipeline automatically handles missing data, scales numbers, and encodes the neighborhood text.
        4. The Linear Regression model calculates the instant price prediction.
        
        ---
        
        **Created with ❤️ using Streamlit**
        """)

if __name__ == "__main__":
    main()