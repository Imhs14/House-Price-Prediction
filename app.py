"""
Streamlit App for House Price Prediction
"""
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import plotly.graph_objects as go
import plotly.express as px
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
def load_model_and_scaler():
    """Load the trained model and scaler"""
    try:
        model = joblib.load('models/house_price_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        with open('models/metrics.json', 'r') as f:
            metrics = json.load(f)
        return model, scaler, metrics
    except FileNotFoundError:
        st.error("⚠️ Model files not found. Please run train.py first!")
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
    st.markdown("### Predict house prices using Linear Regression")
    st.markdown("---")
    
    # Load model and scaler
    model, scaler, metrics = load_model_and_scaler()
    
    # Sidebar
    st.sidebar.header("📊 Model Information")
    st.sidebar.markdown(f"""
    **Model Type:** Linear Regression  
    **Training Date:** Latest  
    **Features:** 7 input variables
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
            square_feet = st.number_input(
                "Square Feet 📐",
                min_value=500,
                max_value=10000,
                value=2000,
                step=100,
                help="Total square footage of the house"
            )
            
            bedrooms = st.slider(
                "Number of Bedrooms 🛏️",
                min_value=1,
                max_value=10,
                value=3,
                help="Number of bedrooms in the house"
            )
            
            bathrooms = st.slider(
                "Number of Bathrooms 🚿",
                min_value=1,
                max_value=8,
                value=2,
                help="Number of bathrooms in the house"
            )
            
            age = st.number_input(
                "Age of House (years) 📅",
                min_value=0,
                max_value=200,
                value=10,
                step=1,
                help="Age of the house in years"
            )
        
        with col2:
            garage_spaces = st.slider(
                "Garage Spaces 🚗",
                min_value=0,
                max_value=5,
                value=2,
                help="Number of garage parking spaces"
            )
            
            lot_size = st.number_input(
                "Lot Size (sq ft) 🏡",
                min_value=1000,
                max_value=50000,
                value=8000,
                step=500,
                help="Total lot size in square feet"
            )
            
            neighborhood_score = st.slider(
                "Neighborhood Score ⭐",
                min_value=1.0,
                max_value=10.0,
                value=7.0,
                step=0.1,
                help="Neighborhood quality score (1-10)"
            )
        
        st.markdown("---")
        
        # Prediction button
        if st.button("🔮 Predict House Price"):
            # Prepare input data
            input_data = pd.DataFrame({
                'square_feet': [square_feet],
                'bedrooms': [bedrooms],
                'bathrooms': [bathrooms],
                'age': [age],
                'garage_spaces': [garage_spaces],
                'lot_size': [lot_size],
                'neighborhood_score': [neighborhood_score]
            })
            
            # Scale input
            input_scaled = scaler.transform(input_data)
            
            # Make prediction
            prediction = model.predict(input_scaled)[0]
            
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
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Square Feet", f"{square_feet:,}")
            col2.metric("Bedrooms", bedrooms)
            col3.metric("Bathrooms", bathrooms)
            col4.metric("Age", f"{age} years")
            
            col5, col6, col7 = st.columns(3)
            col5.metric("Garage", f"{garage_spaces} spaces")
            col6.metric("Lot Size", f"{lot_size:,} sq ft")
            col7.metric("Neighborhood", f"{neighborhood_score}/10")
            
            # Price range estimate
            st.markdown("### 📊 Price Range Estimate")
            lower_bound = prediction * 0.9
            upper_bound = prediction * 1.1
            
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
        
        This application uses **Linear Regression** to predict house prices based on various features.
        
        #### 📊 Features Used for Prediction:
        1. **Square Feet**: Total living area of the house
        2. **Bedrooms**: Number of bedrooms
        3. **Bathrooms**: Number of bathrooms
        4. **Age**: Age of the house in years
        5. **Garage Spaces**: Number of parking spaces
        6. **Lot Size**: Total property size
        7. **Neighborhood Score**: Quality rating of the neighborhood (1-10)
        
        #### 🔧 Technology Stack:
        - **Machine Learning**: Scikit-learn (Linear Regression)
        - **Data Processing**: Pandas, NumPy
        - **Visualization**: Plotly, Matplotlib, Seaborn
        - **Web Framework**: Streamlit
        - **Model Persistence**: Joblib
        
        #### 📈 How It Works:
        1. Input house features using the sliders and input fields
        2. Click the "Predict House Price" button
        3. The model processes your input using the trained Linear Regression model
        4. Get an instant price prediction with confidence range
        
        #### ⚠️ Disclaimer:
        This is a demonstration project. Predictions are based on synthetic data and should not be used for actual real estate decisions.
        
        ---
        
        **Created with ❤️ using Streamlit**
        """)

if __name__ == "__main__":
    main()
