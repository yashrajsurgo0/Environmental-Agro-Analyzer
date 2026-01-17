# 🚀 COMPLETE SETUP & EXECUTION GUIDE

## Full-Stack Agricultural Data Analysis Platform

**Status**: ✅ Ready for Development  
**Date**: January 17, 2026  
**Components**: Backend (Flask) + Frontend (React)

---

## 📋 PROJECT OVERVIEW

This is a **complete end-to-end application** that allows you to:

1. **Upload** agricultural data (CSV files)
2. **Analyze** data with statistics and correlations
3. **Train** ML models (Linear Regression & Random Forest)
4. **Visualize** results with interactive charts
5. **Compare** model performance

### Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: React (JavaScript)
- **Charting**: Recharts
- **ML**: Scikit-learn
- **Data**: Pandas, NumPy

---

## 🎯 WHAT YOU HAVE

### 1. Real Dataset (5 Years)
**File**: `maharashtra_agricultural_data.csv`
- ✅ Real Maharashtra agricultural data (2019-2023)
- ✅ 50 records from Nashik & Pune districts
- ✅ 5 crop types (Wheat, Rice, Corn, Sugarcane, Cotton)
- ✅ Climate variables + market data

### 2. Updated Jupyter Notebook
**File**: `Climate_Agricultural_Markets.ipynb`
- ✅ Now uses REAL Maharashtra data
- ✅ All visualizations work with real data
- ✅ Automatically loads CSV if available
- ✅ Fallback to synthetic data if needed

### 3. Complete Web Application
**Folder**: `webapp/`
- ✅ Backend API (Flask)
- ✅ Frontend UI (React)
- ✅ All components ready
- ✅ Styling included

---

## 🏗️ PROJECT STRUCTURE

```
PROJECT/
├── Climate_Agricultural_Markets.ipynb    ← Updated with real data
├── maharashtra_agricultural_data.csv     ← REAL DATA (2019-2023)
├── WEBAPP_README.md                      ← App documentation
│
└── webapp/
    ├── setup.sh                          ← Setup script
    ├── backend/
    │   ├── app.py                        ← Flask API
    │   ├── requirements.txt              ← Python packages
    │   └── uploads/                      ← CSV uploads
    │
    └── frontend/
        ├── package.json                  ← Node packages
        ├── public/
        │   └── index.html
        ├── App.js                        ← Main component
        ├── App.css                       ← Styling
        ├── index.js
        └── components/
            ├── FileUpload.js
            ├── DataAnalysis.js
            ├── ModelComparison.js
            └── Visualizations.js
```

---

## 📦 PREREQUISITES

Before starting, make sure you have:

### 1. Python 3.7+
```bash
python3 --version
```
If not installed:
- **Mac**: `brew install python3`
- **Windows**: Download from https://python.org/
- **Linux**: `sudo apt install python3`

### 2. Node.js & npm
```bash
node --version
npm --version
```
If not installed:
- Download from https://nodejs.org/

### 3. Git (optional but recommended)
```bash
git --version
```

---

## 🚀 QUICK START (5 Minutes)

### Method 1: Automatic Setup (Recommended)

**On Mac/Linux:**
```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
chmod +x webapp/setup.sh
bash webapp/setup.sh
```

**On Windows:**
```cmd
cd Desktop/PROJECT
python -m pip install --upgrade pip
cd webapp/backend && pip install -r requirements.txt
cd ../frontend && npm install && npm install recharts
```

### Method 2: Manual Setup

**Step 1: Install Backend**
```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/backend
pip install -r requirements.txt
```

**Step 2: Install Frontend**
```bash
cd ../frontend
npm install
npm install recharts
```

**Step 3: Start Backend** (Terminal 1)
```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/backend
python app.py
```

**Step 4: Start Frontend** (Terminal 2)
```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/frontend
npm start
```

**Step 5: Open Application**
```
http://localhost:3000
```

---

## 📊 USING THE APPLICATION

### Step 1: Upload Data

1. Open `http://localhost:3000`
2. Click **"📤 Upload CSV"**
3. Select a CSV file with these columns:
   - Year
   - Crop
   - Rainfall_mm
   - Avg_Temperature_C
   - Crop_Yield
   - Market_Price

**Example**: Use `maharashtra_agricultural_data.csv` (already in project)

### Step 2: Analyze

1. Click **"📊 Analyze Data"** button
2. Wait for processing (30-60 seconds)
3. View results:
   - Data statistics
   - Model metrics
   - Visualizations

### Step 3: Review Results

You'll see:
- **Data Analysis**: Statistics for each feature
- **Model Comparison**: Linear Regression vs Random Forest
- **Visualizations**: 
  - Rainfall trends
  - Temperature trends
  - Rainfall vs Crop Yield (scatter plot)
  - Crop-wise statistics
  - Feature importance
  - Model comparison charts

---

## 🧪 TESTING WITH REAL DATA

### Using Included Maharashtra Data

```bash
# The data is already in the project:
# maharashtra_agricultural_data.csv

# Open the app and upload this file
# It contains 50 real records from 2019-2023
```

### Using Your Own Data

**Create a CSV file** with this format:

```csv
Year,Crop,Rainfall_mm,Avg_Temperature_C,Crop_Yield,Market_Price
2019,Wheat,450.5,18.2,2850,250.50
2019,Rice,850.3,22.5,4200,180.75
2020,Corn,650.2,20.1,3800,220.00
```

Then upload through the web interface.

---

## 🔧 DEVELOPMENT WORKFLOW

### Testing Backend Only

```bash
cd webapp/backend
python app.py
```

Test endpoints:
```bash
# Health check
curl http://localhost:5000/api/health

# Download sample template
curl http://localhost:5000/api/download-sample

# Upload file
curl -X POST -F "file=@data.csv" http://localhost:5000/api/upload

# Analyze
curl -X POST http://localhost:5000/api/analyze

# Get results
curl http://localhost:5000/api/results
```

### Modifying Frontend

Edit files in `webapp/frontend/`:
- `App.js` - Main component
- `App.css` - Styling
- `components/*.js` - Feature components

Changes will auto-reload (hot reload enabled).

### Modifying Backend

Edit `webapp/backend/app.py` and restart:
```bash
# Stop: Ctrl+C
# Start: python app.py
```

---

## 📈 USING NOTEBOOK WITH REAL DATA

### Option 1: Run via Jupyter

```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
jupyter notebook Climate_Agricultural_Markets.ipynb
```

Then:
1. Press `Cmd+Shift+Enter` (Mac) or `Ctrl+Shift+Enter` (Windows)
2. All 29 cells execute
3. Results display inline

### Option 2: Run via Command Line

```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
python -m nbconvert --to notebook --execute Climate_Agricultural_Markets.ipynb
```

---

## 🎯 API ENDPOINTS REFERENCE

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/health` | Check server status |
| POST | `/api/upload` | Upload CSV file |
| POST | `/api/analyze` | Analyze data & train models |
| GET | `/api/results` | Get analysis results |
| GET | `/api/stats` | Get data statistics |
| GET | `/api/download-sample` | Get sample CSV template |

### Example: Using API with Python

```python
import requests
import json

# Upload file
files = {'file': open('data.csv', 'rb')}
response = requests.post('http://localhost:5000/api/upload', files=files)
print(response.json())

# Analyze
response = requests.post('http://localhost:5000/api/analyze')
results = response.json()
print(json.dumps(results, indent=2))
```

---

## 🐛 TROUBLESHOOTING

### Port Already in Use

If you get "Address already in use" error:

**Mac/Linux:**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

**Windows:**
```cmd
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Module Not Found

If you get "ModuleNotFoundError":

```bash
# Make sure you're in the backend folder
cd webapp/backend

# Reinstall requirements
pip install -r requirements.txt
```

### npm ERR! 404

If npm packages won't install:

```bash
cd webapp/frontend

# Clear cache
npm cache clean --force

# Reinstall
npm install
npm install recharts
```

### CSV Upload Error

**Problem**: "Missing required columns"

**Solution**: Ensure your CSV has exactly these columns (case-sensitive):
- Year
- Crop
- Rainfall_mm
- Avg_Temperature_C
- Crop_Yield
- Market_Price

### Analysis Fails

**Problem**: "Analysis failed" error

**Solution**:
1. Check CSV has no empty cells in numeric columns
2. Ensure numeric columns have numeric data
3. Try with included `maharashtra_agricultural_data.csv`

---

## 💡 USEFUL COMMANDS

```bash
# Backend
cd webapp/backend
python app.py                          # Start server
pip install -r requirements.txt        # Install deps
pip list                               # Check installed packages

# Frontend
cd webapp/frontend
npm start                              # Start dev server
npm install <package>                  # Install package
npm run build                          # Build for production

# Project
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
jupyter notebook                       # Open Jupyter
python -c "import pandas; print(pandas.__version__)"  # Check version
```

---

## 📚 FILE LOCATIONS

| File | Location | Purpose |
|------|----------|---------|
| Notebook | `/Project/Climate_Agricultural_Markets.ipynb` | Jupyter analysis |
| Dataset | `/Project/maharashtra_agricultural_data.csv` | Real data (50 records) |
| Backend | `/Project/webapp/backend/app.py` | Flask API |
| Frontend | `/Project/webapp/frontend/App.js` | React UI |
| Docs | `/Project/WEBAPP_README.md` | App documentation |
| This Guide | `/Project/WEBAPP_SETUP_GUIDE.md` | Setup instructions |

---

## 🎓 NEXT STEPS

### After Setup

1. **Test with included data**:
   - Upload `maharashtra_agricultural_data.csv`
   - Click "Analyze Data"
   - View results

2. **Try with your own data**:
   - Prepare CSV with required columns
   - Upload through web app
   - Analyze and visualize

3. **Explore the code**:
   - Modify visualizations
   - Add new analysis features
   - Improve ML models

4. **Production deployment**:
   - Build frontend: `npm run build`
   - Deploy backend to cloud (Heroku, AWS, etc.)
   - Set up database for storing analyses

---

## 📊 REAL DATA INCLUDED

**File**: `maharashtra_agricultural_data.csv`

### Data Contents:
- **Years**: 2019-2023 (5 years)
- **Crops**: Wheat, Rice, Corn, Sugarcane, Cotton
- **Districts**: Nashik & Pune
- **Records**: 50 total
- **Variables**:
  - Year (2019-2023)
  - Crop (5 types)
  - Rainfall_mm (300-980 mm)
  - Avg_Temperature_C (17.5-26°C)
  - Crop_Yield (1450-5350 units)
  - Market_Price (135-390 currency)
  - Humidity_Percent (44-74%)

### Sample Records:
```
2019,Wheat,Nashik,450.5,18.2,2850,250.50,55
2019,Rice,Nashik,850.3,22.5,4200,180.75,70
2023,Cotton,Pune,630.3,24.8,1700,380.00,49
```

---

## ✅ VERIFICATION CHECKLIST

After setup, verify:

- [ ] Python 3.7+ installed: `python3 --version`
- [ ] Node.js installed: `node --version`
- [ ] Backend dependencies installed: `pip list | grep pandas`
- [ ] Frontend dependencies installed: `npm list react`
- [ ] Backend starts: `python app.py` shows "Running on http://0.0.0.0:5000"
- [ ] Frontend starts: `npm start` shows "Compiled successfully"
- [ ] App opens: `http://localhost:3000` loads
- [ ] Can upload CSV: File upload works
- [ ] Can analyze: Results display
- [ ] Charts display: Visualizations render

---

## 🎉 YOU'RE ALL SET!

Your full-stack agricultural analysis platform is ready!

### Start Here:
```bash
# Terminal 1
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/backend
python app.py

# Terminal 2
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/frontend
npm start

# Browser
http://localhost:3000
```

### Questions?
1. Check troubleshooting section
2. Verify prerequisites
3. Review API endpoints
4. Check included documentation

---

**Happy analyzing! 🌾📊🚀**

Generated: January 17, 2026  
Platform: Agricultural Data Analysis  
Status: ✅ Ready to Deploy
