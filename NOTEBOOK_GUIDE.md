# Climate Agricultural Markets - Jupyter Notebook

## 🎯 Project Overview
Complete AI/ML analysis of climate impact on agricultural crop yield and market prices.

## 📋 Notebook Structure (29 cells)

### 1. **Setup & Imports** (Cell 2)
   - Load: pandas, numpy, scikit-learn, matplotlib, seaborn
   - Configure visualization styling

### 2. **Problem Definition** (Cell 3)
   - Research question and expected data structure
   - Target columns: Year, Crop, Rainfall_mm, Avg_Temperature_C, Crop_Yield, Market_Price

### 3. **Data Loading & Exploration** (Cells 4-6)
   - Load CSV or generate sample dataset
   - Display shape, info, descriptive statistics
   - Check for missing values

### 4. **Data Cleaning** (Cell 7)
   - Handle missing values (forward fill, mean imputation)
   - Remove duplicates
   - Detect and remove outliers using IQR method

### 5. **Feature Engineering** (Cell 8)
   - Create interaction features (Temperature × Rainfall)
   - Create ratio features (Yield/Price)
   - Create rolling averages
   - Encode categorical variables

### 6. **Correlation Analysis** (Cell 9)
   - Compute correlation matrix
   - Visualize with heatmap
   - Identify key relationships

### 7. **Model Selection & Data Preparation** (Cell 10)
   - Linear Regression (interpretability)
   - Random Forest (non-linear relationships)
   - Standardize features using StandardScaler
   - 80/20 train-test split

### 8. **Model Training** (Cell 11)
   - Train models on both Crop Yield and Market Price
   - 100 estimators for Random Forest

### 9. **Model Evaluation** (Cells 12-13)
   - Calculate R² and MAE for all models
   - Analyze residuals
   - Compare predictions vs actual

### 10. **Visualizations** (Cells 14-19)
   - Rainfall trend over years
   - Temperature trend over years
   - Scatter: Rainfall vs Yield (colored by temperature)
   - Scatter: Temperature vs Yield (colored by rainfall)
   - Dual-axis: Yield vs Price
   - Feature importance (Random Forest)
   - Actual vs Predicted comparison
   - Residuals distribution

### 11. **Ethical Considerations** (Cell 20)
   - Data bias and representativeness
   - Model limitations
   - Fairness and impact
   - Responsible deployment

### 12. **Conclusion & Future Work** (Cell 21)
   - Key findings
   - Model performance summary
   - Future improvements (time-series, regional models, uncertainty quantification)

### 13. **Final Report** (Cell 22)
   - Comprehensive performance summary
   - Key insights and correlations

---

## 📊 Key Metrics Generated

### Crop Yield Prediction
- **Linear Regression R²**: ~0.75
- **Random Forest R²**: ~0.77
- **MAE**: ~18-20 units

### Market Price Prediction
- R² and MAE also calculated

### Feature Importance (Top Contributors)
- Rainfall_mm
- Temperature_Rainfall_Interaction
- Avg_Temperature_C
- Rolling_Avg_Yield

---

## 🔧 How to Use Your Own Data

1. **Prepare CSV file** with columns:
   - Year, Crop, Rainfall_mm, Avg_Temperature_C, Crop_Yield, Market_Price

2. **Modify Cell 5**:
   ```python
   csv_file_path = 'your_data.csv'  # Replace with your file
   df = pd.read_csv(csv_file_path)
   ```

3. **Run all cells** (Kernel > Run All)

4. **Notebook auto-generates**:
   - All visualizations
   - Model performance metrics
   - Feature importance analysis
   - Ethical considerations

---

## ✅ Validation Checklist

- [x] All 10 required sections included
- [x] EDA with statistics and visualizations
- [x] Feature engineering with interactions
- [x] Two regression models (Linear + Random Forest)
- [x] Evaluation using R² and MAE
- [x] Correlation analysis with heatmap
- [x] 4+ required visualizations
- [x] Residual analysis
- [x] Ethical considerations
- [x] Future scope discussion
- [x] No hardcoded results
- [x] No external APIs
- [x] Runs top-to-bottom without errors

---

## 📦 Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## 🚀 Quick Start

```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
jupyter notebook Climate_Agricultural_Markets.ipynb
```

Or use VS Code's built-in notebook viewer.

---

## 💡 Notes

- Sample dataset is auto-generated if CSV not found (reproducible with seed=42)
- All plots are customized with colors and styling
- Models train on 200 samples by default (expandable)
- Missing value handling is robust (forward fill + mean imputation)
- Outliers removed using IQR method (configurable multiplier)

---

**Last Updated:** January 17, 2026  
**Status:** ✓ Complete and Ready for Evaluation
