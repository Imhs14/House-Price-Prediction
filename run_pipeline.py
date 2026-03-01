#!/usr/bin/env python3
"""
Quick Start Script - Run the entire pipeline
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and display status"""
    print("\n" + "="*60)
    print(f"📋 {description}")
    print("="*60)
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}")
        print(e.stdout)
        print(e.stderr)
        return False

def main():
    print("\n" + "="*60)
    print("🏠 HOUSE PRICE PREDICTION - QUICK START")
    print("="*60)
    
    steps = [
        ("python generate_data.py", "Step 1: Generating Dataset"),
        ("python src/train_model.py", "Step 2: Training Model"),
        ("python notebooks/eda.py", "Step 3: Running EDA (Optional)"),
    ]
    
    for command, description in steps:
        if not run_command(command, description):
            print(f"\n❌ Pipeline stopped at: {description}")
            sys.exit(1)
    
    print("\n" + "="*60)
    print("✨ ALL STEPS COMPLETED SUCCESSFULLY!")
    print("="*60)
    print("\n🚀 To launch the web app, run:")
    print("   streamlit run app.py")
    print("\n📊 Generated files:")
    print("   - data/house_prices.csv")
    print("   - data/train.csv")
    print("   - data/test.csv")
    print("   - models/house_price_model.pkl")
    print("   - models/scaler.pkl")
    print("   - models/metrics.csv")
    print("   - models/model_performance.png")
    print("   - data/eda_visualization.png")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    # Check if we're in the right directory
    if not os.path.exists("requirements.txt"):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    main()
