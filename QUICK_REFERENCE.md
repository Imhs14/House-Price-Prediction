# 🚀 Quick Reference Card

## Essential Commands

### Setup (One Time)
```bash
cd house_price_prediction
pip install -r requirements.txt
```

### Generate Data
```bash
python generate_data.py
```

### Train Model
```bash
python train.py
```

### Launch App
```bash
streamlit run app.py
```

## File Structure

```
📦 house_price_prediction
 ┣ 📂 data/                    # Datasets
 ┣ 📂 models/                  # Trained models
 ┣ 📂 notebooks/               # Visualizations
 ┣ 📂 src/                     # Source code
 ┣ 📜 app.py                   # Streamlit app
 ┣ 📜 train.py                 # Training pipeline
 ┣ 📜 generate_data.py         # Data generation
 ┣ 📜 requirements.txt         # Dependencies
 ┗ 📜 README.md                # Documentation
```

## Model Features

| Feature | Range | Impact |
|---------|-------|--------|
| Square Feet | 500-10,000 | ⭐⭐⭐⭐⭐ High |
| Bedrooms | 1-10 | ⭐⭐⭐ Medium |
| Bathrooms | 1-8 | ⭐⭐ Low-Medium |
| Age | 0-200 | ⭐⭐ Negative |
| Garage | 0-5 | ⭐⭐ Low-Medium |
| Lot Size | 1k-50k | ⭐⭐⭐ Medium |
| Neighborhood | 1-10 | ⭐⭐⭐⭐ High |

## Performance Metrics

- **R² Score**: 0.9767 (Excellent!)
- **RMSE**: $29,360
- **MAE**: $22,782

## Common Issues

**Import Error?**
→ Run: `pip install -r requirements.txt`

**File Not Found?**
→ Run: `python train.py` first

**Port Busy?**
→ Use: `streamlit run app.py --server.port 8502`

## Key Files

- **app.py** - Web interface
- **train.py** - Model training
- **README.md** - Full documentation
- **USAGE_GUIDE.md** - Step-by-step guide

## Streamlit Tips

- Press **R** to rerun app
- Press **C** to clear cache
- Use sidebar for navigation
- Check "Performance" tab for metrics

## Documentation

1. **README.md** - Overview & setup
2. **USAGE_GUIDE.md** - Detailed instructions
3. **ARCHITECTURE.md** - Technical details
4. **PROJECT_SUMMARY.md** - What's included

## Example Prediction

```
Input:
  Square Feet: 2500
  Bedrooms: 4
  Bathrooms: 3
  Age: 5
  Garage: 2
  Lot Size: 8000
  Neighborhood: 7.5

Output:
  Predicted Price: ~$748,523
```

## Support

📧 Check documentation files
🐛 Review error messages
💡 Try different inputs
🔄 Retrain if needed

---
**Built with:** Python • Scikit-learn • Streamlit
