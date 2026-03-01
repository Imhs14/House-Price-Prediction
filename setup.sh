#!/bin/bash

echo "=================================="
echo "House Price Prediction - Quick Start"
echo "=================================="
echo ""

echo "Step 1: Installing dependencies..."
pip install -r requirements.txt --break-system-packages

echo ""
echo "Step 2: Generating dataset..."
python generate_data.py

echo ""
echo "Step 3: Training model..."
python train.py

echo ""
echo "=================================="
echo "Setup Complete!"
echo "=================================="
echo ""
echo "To run the Streamlit app, use:"
echo "  streamlit run app.py"
echo ""
