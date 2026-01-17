# 🌾 Agricultural Data Analysis Platform

A full-stack web application for uploading, analyzing, and visualizing agricultural climate data with machine learning models.

## ✨ Features

✅ **CSV File Upload** - Upload agricultural data with validation  
✅ **Data Analysis** - Comprehensive statistics and correlations  
✅ **ML Models** - Linear Regression & Random Forest (100 trees)  
✅ **Real-time Visualizations** - Interactive charts and graphs  
✅ **Model Comparison** - Compare performance metrics  
✅ **Responsive Design** - Works on desktop and mobile  

## 📋 Required CSV Format

Your CSV file must contain these columns:

```
Year,Crop,Rainfall_mm,Avg_Temperature_C,Crop_Yield,Market_Price
2019,Wheat,450.5,18.2,2850,250.50
2019,Rice,850.3,22.5,4200,180.75
2020,Corn,650.2,20.1,3800,220.00
```

**Column Descriptions:**
- **Year**: Year of observation (numeric)
- **Crop**: Crop type (text)
- **Rainfall_mm**: Annual rainfall in millimeters
- **Avg_Temperature_C**: Average annual temperature in Celsius
- **Crop_Yield**: Crop yield (numeric)
- **Market_Price**: Market price per unit (numeric)

## 🚀 Quick Start

### Option 1: Full Setup (Development)

#### 1. Install Backend Dependencies
```bash
cd webapp/backend
pip install -r requirements.txt
```

#### 2. Start Backend Server
```bash
python app.py
```
Backend will run on: `http://localhost:5000`

#### 3. Install Frontend Dependencies
```bash
cd webapp/frontend
npm install
npm install recharts  # For charts
```

#### 4. Start Frontend Server
```bash
npm start
```
Frontend will run on: `http://localhost:3000`

#### 5. Access the Application
Open: `http://localhost:3000`

---

### Option 2: Backend Only (API Testing)

```bash
cd webapp/backend
pip install -r requirements.txt
python app.py
```

Test with curl:
```bash
# Health check
curl http://localhost:5000/api/health

# Get sample template
curl http://localhost:5000/api/download-sample
```

---

## 📊 API Endpoints

### Upload File
**POST** `/api/upload`
```bash
curl -X POST -F "file=@data.csv" http://localhost:5000/api/upload
```

### Analyze Data
**POST** `/api/analyze`
```bash
curl -X POST http://localhost:5000/api/analyze
```

### Get Results
**GET** `/api/results`
```bash
curl http://localhost:5000/api/results
```

### Get Statistics
**GET** `/api/stats`
```bash
curl http://localhost:5000/api/stats
```

### Download Sample Template
**GET** `/api/download-sample`
```bash
curl http://localhost:5000/api/download-sample
```

### Health Check
**GET** `/api/health`
```bash
curl http://localhost:5000/api/health
```

---

## 🏗️ Project Structure

```
webapp/
├── backend/
│   ├── app.py                    # Flask API server
│   ├── requirements.txt          # Python dependencies
│   └── uploads/                  # Uploaded files directory
│
└── frontend/
    ├── App.js                    # Main React component
    ├── App.css                   # Styling
    └── components/
        ├── FileUpload.js         # Upload component
        ├── DataAnalysis.js       # Statistics component
        ├── ModelComparison.js    # ML models comparison
        └── Visualizations.js     # Charts component
```

---

## 🎯 How It Works

### 1. Upload
- Select a CSV file with required columns
- File is validated on backend
- Data is stored for processing

### 2. Analyze
- Clean data (remove outliers)
- Calculate statistics
- Train ML models
- Generate visualizations

### 3. Visualize
- Rainfall trends over time
- Temperature trends
- Rainfall vs Crop Yield correlation
- Crop-wise statistics
- Feature importance
- Model performance comparison

### 4. Compare Models
- **Linear Regression**: Fast, interpretable
- **Random Forest**: Better accuracy, 100 trees

---

## 📈 ML Pipeline

```
Raw Data (CSV)
     ↓
[Data Cleaning]
- Remove missing values
- Remove outliers (IQR method)
     ↓
[Feature Engineering]
- Extract rainfall, temperature, etc.
- Standardize features (StandardScaler)
     ↓
[Train-Test Split]
- 80% training, 20% testing
     ↓
[Model Training]
- Linear Regression
- Random Forest (100 estimators)
     ↓
[Evaluation]
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
     ↓
[Predictions & Visualization]
```

---

## 📊 Performance Metrics

### Linear Regression
- **R² Score**: Proportion of variance explained
- **MAE**: Average prediction error
- **RMSE**: Root of squared errors
- **Coefficients**: Feature weights

### Random Forest
- **R² Score**: Typically higher than Linear Regression
- **MAE**: Often lower than Linear Regression
- **RMSE**: Better error distribution
- **Feature Importance**: Relative importance of each feature

---

## 🔍 Example Usage

### 1. Prepare Your Data
Create `my_data.csv`:
```csv
Year,Crop,Rainfall_mm,Avg_Temperature_C,Crop_Yield,Market_Price
2019,Wheat,450,18.2,2850,250
2019,Rice,850,22.5,4200,180
2020,Wheat,480,18.5,2920,265
```

### 2. Start Application
```bash
# Terminal 1: Backend
cd webapp/backend && python app.py

# Terminal 2: Frontend
cd webapp/frontend && npm start
```

### 3. Upload & Analyze
1. Open `http://localhost:3000`
2. Click "📤 Upload CSV"
3. Select your `my_data.csv`
4. Click "📊 Analyze Data"
5. View results!

---

## 🛠️ Troubleshooting

### CSV Upload Error
- **Check columns**: Must have Year, Crop, Rainfall_mm, Avg_Temperature_C, Crop_Yield, Market_Price
- **Check data types**: Numeric columns should be numbers
- **Max size**: 50MB limit

### Analysis Fails
- **Empty data**: Upload a file first
- **Invalid data**: Check for missing values in numeric columns
- **Memory**: For large datasets (>1M rows), may need more RAM

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

---

## 📦 Dependencies

### Backend (Python)
- Flask 2.3.3
- pandas 1.5.3
- numpy 1.24.3
- scikit-learn 1.3.0
- matplotlib 3.7.2
- seaborn 0.12.2

### Frontend (JavaScript)
- React
- recharts (charting library)

---

## 📝 Sample Responses

### Successful Upload
```json
{
  "message": "File uploaded successfully",
  "filename": "data.csv",
  "rows": 50,
  "columns": 6,
  "columns_list": ["Year", "Crop", "Rainfall_mm", "Avg_Temperature_C", "Crop_Yield", "Market_Price"]
}
```

### Analysis Result
```json
{
  "message": "Analysis completed successfully",
  "analysis": {
    "descriptive_stats": {...},
    "correlations": {...}
  },
  "models": {
    "linear_regression": {
      "r2_score": 0.523,
      "mae": 245.68,
      "rmse": 312.46
    },
    "random_forest": {
      "r2_score": 0.712,
      "mae": 187.23,
      "rmse": 234.57
    }
  },
  "visualizations": {
    "rainfall_trend": {...},
    "feature_importance": {...}
  }
}
```

---

## 🎓 Learning Resources

- **Scikit-learn Docs**: https://scikit-learn.org/
- **Flask Docs**: https://flask.palletsprojects.com/
- **React Docs**: https://react.dev/
- **Recharts**: https://recharts.org/

---

## 📄 License

Open source project for educational purposes.

---

## 🤝 Contributing

Feel free to:
- Add new visualizations
- Improve models
- Enhance frontend UI
- Add more analysis features

---

## 📞 Support

For issues or questions:
1. Check troubleshooting section
2. Verify CSV format
3. Check browser console for errors
4. Review Flask logs

---

**Created**: January 17, 2026  
**Purpose**: Agricultural climate and market analysis with ML  
**Status**: ✅ Ready to Use

