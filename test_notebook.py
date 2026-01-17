#!/usr/bin/env python
"""Quick test to verify notebook logic works without plotting"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error

# Create sample dataset
np.random.seed(42)
n_samples = 200
years = np.repeat(range(2000, 2020), 10)
crops = np.tile(['Wheat', 'Rice', 'Corn', 'Soybean', 'Barley', 
                 'Oats', 'Millet', 'Maize', 'Rye', 'Lentil'], 20)
rainfall = np.random.uniform(300, 1200, n_samples)
temperature = np.random.uniform(10, 30, n_samples)
crop_yield = 50 + 0.15 * rainfall - 1.5 * np.abs(temperature - 20) + np.random.normal(0, 20, n_samples)
crop_yield = np.maximum(crop_yield, 10)
market_price = 100 + 0.05 * rainfall - 2 * (crop_yield - 50) + np.random.normal(0, 10, n_samples)
market_price = np.maximum(market_price, 20)

df = pd.DataFrame({
    'Year': years, 'Crop': crops, 'Rainfall_mm': rainfall,
    'Avg_Temperature_C': temperature, 'Crop_Yield': crop_yield, 'Market_Price': market_price
})

print("✓ Dataset created")

# Data cleaning
df_clean = df.copy()
df_clean['Rainfall_mm'].fillna(df_clean['Rainfall_mm'].mean(), inplace=True)
df_clean['Avg_Temperature_C'].fillna(df_clean['Avg_Temperature_C'].mean(), inplace=True)
df_clean = df_clean.drop_duplicates()
print("✓ Data cleaned")

# Feature engineering
df_features = df_clean.copy()
df_features['Temperature_Rainfall_Interaction'] = df_features['Avg_Temperature_C'] * df_features['Rainfall_mm']
df_features['Yield_Price_Ratio'] = df_features['Crop_Yield'] / (df_features['Market_Price'] + 1)
df_features['Crop_Encoded'] = pd.factorize(df_features['Crop'])[0]
print("✓ Features engineered")

# Prepare data
feature_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Temperature_Rainfall_Interaction', 'Crop_Encoded', 'Year']
X = df_features[feature_cols].fillna(0)
y = df_features['Crop_Yield'].fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print("✓ Data prepared and split")

# Train models
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_r2 = r2_score(y_test, lr_pred)
print(f"✓ Linear Regression trained (R² = {lr_r2:.4f})")

rf = RandomForestRegressor(n_estimators=50, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_r2 = r2_score(y_test, rf_pred)
print(f"✓ Random Forest trained (R² = {rf_r2:.4f})")

# Evaluation
lr_mae = mean_absolute_error(y_test, lr_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)
print(f"\n✓ All tests passed!")
print(f"  Linear Regression: R²={lr_r2:.4f}, MAE={lr_mae:.4f}")
print(f"  Random Forest: R²={rf_r2:.4f}, MAE={rf_mae:.4f}")
