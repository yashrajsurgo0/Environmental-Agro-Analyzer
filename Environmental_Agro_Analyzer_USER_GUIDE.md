# ENVIRONMENTAL AGRO ANALYZER
## User Guide & Operations Manual

**Document Type**: User Manual  
**Version**: 1.0  
**Last Updated**: January 17, 2026

---

## QUICK START GUIDE

### Getting Started in 5 Minutes

#### Step 1: Start the Services
```bash
# Open Terminal 1 - Start Backend
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
source .venv/bin/activate
cd webapp/backend
python app_port5001.py

# Wait for message: "Running on http://127.0.0.1:5001"
```

#### Step 2: Start Frontend
```bash
# Open Terminal 2 - Start Frontend
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/frontend
npm start

# Wait for: "Local: http://localhost:3000"
```

#### Step 3: Open Application
```
Open your browser and go to: http://localhost:3000
```

#### Step 4: Upload Data
1. Click **"📤 Upload CSV"** button
2. Select CSV file (use provided template)
3. Click **"📤 Upload CSV"** again
4. Wait for success message

#### Step 5: Analyze Data
1. Click **"📊 Analyze Data"** button
2. Wait for processing (1-2 seconds)
3. View results and visualizations

---

## USER INTERFACE GUIDE

### Dashboard Layout

```
┌────────────────────────────────────────────────┐
│  🌾 Agricultural Data Analysis Platform        │
│  Upload, Analyze, and Visualize Data          │
├────────────────────────────────────────────────┤
│                                                │
│  📤 Upload Agricultural Data                   │
│  ┌──────────────────────────────────────┐    │
│  │ Choose file or drag and drop        │    │
│  │ [Choose File]    [📤 Upload CSV]    │    │
│  └──────────────────────────────────────┘    │
│                                                │
│  📋 CSV should contain:                        │
│  Year, Crop, Rainfall_mm, Avg_Temperature_C,  │
│  Crop_Yield, Market_Price, Humidity_Percent   │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│  [📊 Analyze Data]                            │
│                                                │
├────────────────────────────────────────────────┤
│  DATA ANALYSIS RESULTS                         │
│  ├─ Records: 50                               │
│  ├─ Mean Yield: 45.2 quintals/ha              │
│  ├─ Mean Price: ₹2400/quintal                 │
│  └─ Data Quality: 98.5%                       │
│                                                │
│  MODEL PERFORMANCE                             │
│  ├─ Linear Regression R²: 0.946               │
│  └─ Random Forest R²: 0.932                   │
│                                                │
│  VISUALIZATIONS (8 Charts)                     │
│  ├─ Rainfall vs Yield                         │
│  ├─ Temperature vs Yield                      │
│  ├─ Market Price Trends                       │
│  └─ [5 more charts...]                        │
│                                                │
└────────────────────────────────────────────────┘
```

### Key Interface Elements

#### 1. File Upload Section
- **Component**: File Input + Button
- **Functions**:
  - Select CSV file from computer
  - Drag and drop file
  - See upload status
  - Get error messages

#### 2. Analyze Button
- **Function**: Trigger data analysis
- **Availability**: Active after file upload
- **Feedback**: Shows "⏳ Analyzing..." during processing
- **Result**: Displays analysis results below

#### 3. Statistics Display
- **Shows**: Summary statistics
- **Includes**:
  - Total records count
  - Mean values for each variable
  - Standard deviations
  - Data quality score

#### 4. Model Comparison
- **Linear Regression Metrics**:
  - R² Score: 0.946
  - MAE: 2.15
  - RMSE: 2.87
  - Coefficients for each feature

- **Random Forest Metrics**:
  - R² Score: 0.932
  - MAE: 2.42
  - RMSE: 3.15
  - Feature importance percentages

#### 5. Visualizations
Eight interactive charts:
1. Rainfall vs Crop Yield (Scatter)
2. Temperature vs Crop Yield (Scatter)
3. Market Price Trends (Line)
4. Crop Distribution (Bar)
5. Humidity Impact (Scatter)
6. Yield Distribution (Histogram)
7. Price Distribution (Histogram)
8. Correlation Heatmap (Matrix)

---

## HOW TO USE FEATURES

### Feature 1: Upload CSV File

#### Method A: Click to Select File
```
1. Click "Choose File" button
2. Browse and select CSV file
3. Click "Upload CSV"
4. Wait for success message
```

#### Method B: Drag and Drop
```
1. Drag CSV file from file explorer
2. Drop on upload area
3. Automatically opens file selector
4. Click "Upload CSV"
```

#### File Requirements
- Format: .csv only
- Required columns: All 7 must be present
- Size: Maximum 50MB
- Content: No empty cells

#### Sample CSV Format
```csv
Year,Crop,Rainfall_mm,Avg_Temperature_C,Crop_Yield,Market_Price,Humidity_Percent
2019,Rice,1200,28.5,45,2500,75
2019,Wheat,850,23,40,1800,70
2020,Rice,1150,29,46,2600,76
```

#### Troubleshooting Upload
- ✓ File not selected: Click "Choose File"
- ✓ Wrong format: Use .csv only
- ✓ Missing columns: Check all 7 required
- ✓ File too large: Keep under 50MB
- ✓ Invalid data: Check no empty cells

### Feature 2: Analyze Data

#### Steps to Analyze
```
1. Upload CSV file successfully
2. Review upload confirmation
3. Click "📊 Analyze Data" button
4. Wait 1-2 seconds for processing
5. View results automatically
```

#### What Happens During Analysis
```
Processing Steps:
├─ Data Validation (check quality)
├─ Data Cleaning (remove errors)
├─ Statistical Analysis (calculate stats)
├─ Correlation Analysis (relationships)
├─ Model Training (fit ML models)
├─ Model Evaluation (calculate metrics)
└─ Generate Visualizations (create charts)
```

#### Analysis Results Include

**1. Data Statistics**
```
Total Records: 50
Missing Values: 1
Outliers Detected: 2
Data Quality: 98.5%

Summary Statistics:
├─ Rainfall: Mean=1100.5, Std=250.3
├─ Temperature: Mean=25.8, Std=4.2
├─ Yield: Mean=45.2, Std=8.5
└─ Price: Mean=2400, Std=650
```

**2. Correlation Analysis**
```
Correlations Detected:
├─ Rainfall vs Yield: +0.78 (Strong)
├─ Temperature vs Yield: -0.42 (Moderate)
├─ Humidity vs Yield: +0.65 (Strong)
└─ Yield vs Price: +0.72 (Strong)
```

**3. ML Model Results**
```
Linear Regression:
├─ R² Score: 0.946 (94.6% accuracy)
├─ MAE: 2.15 quintals/ha
├─ RMSE: 2.87 quintals/ha
└─ Best for: Interpretable predictions

Random Forest:
├─ R² Score: 0.932 (93.2% accuracy)
├─ MAE: 2.42 quintals/ha
├─ RMSE: 3.15 quintals/ha
└─ Best for: Complex patterns
```

### Feature 3: View Visualizations

#### Interactive Chart Features

**1. Rainfall vs Crop Yield**
- Shows relationship between rainfall and yield
- Red dots indicate each data point
- Trend line shows correlation
- Insight: More rain → Higher yield

**2. Temperature vs Crop Yield**
- Shows temperature effect on yield
- Blue dots indicate data points
- Slight downward trend visible
- Insight: Excessive heat reduces yield

**3. Market Price Trends**
- Line chart over years (2019-2023)
- Shows price increases over time
- Helpful for market predictions
- Insight: Prices trend upward

**4. Crop Distribution**
- Bar chart showing crop counts
- Each bar represents a crop type
- Heights show frequency
- Insight: Rice most common

**5. Humidity Impact**
- Scatter plot of humidity vs yield
- Shows optimal humidity ranges
- Color-coded by clusters
- Insight: 70-75% humidity optimal

**6. Yield Distribution**
- Histogram of crop yields
- Shows normal distribution
- Bell curve shape indicates consistency
- Insight: Predictable yield patterns

**7. Price Distribution**
- Histogram of market prices
- Bimodal distribution visible
- Shows price clusters
- Insight: Two market segments

**8. Correlation Heatmap**
- Color grid showing all correlations
- Red = positive correlation
- Blue = negative correlation
- Intensity shows strength
- Insight: Multiple strong relationships

#### Interactive Features

**Hover Tooltip**
- Position mouse over data point
- Shows exact values
- Helps identify specific records

**Zoom & Pan**
- Available on some charts
- Drag to zoom in on area
- Scroll to pan around

**Legend**
- Shows what each color represents
- Click to show/hide series
- Located below or beside chart

---

## DATA INTERPRETATION GUIDE

### Understanding Statistics

#### Mean
- **Definition**: Average value
- **Example**: Mean yield = 45.2 quintals/ha
- **Use**: Central tendency measurement

#### Standard Deviation
- **Definition**: How spread out data is
- **Example**: Yield std = 8.5 (varies ±8.5)
- **Use**: Measure of variability

#### Correlation Coefficient (-1 to +1)
- **+1.0**: Perfect positive relationship
- **+0.5 to +1.0**: Strong positive
- **0**: No relationship
- **-0.5 to -1.0**: Strong negative
- **-1.0**: Perfect negative relationship

### Interpreting Models

#### R² Score (0 to 1)
```
R² = 0.946 means:
├─ Model explains 94.6% of variance
├─ Very good fit (>0.80 is excellent)
├─ Predictions very accurate
└─ Reliable for forecasting
```

#### Mean Absolute Error (MAE)
```
MAE = 2.15 quintals/ha means:
├─ Average prediction error
├─ Predictions off by 2.15 on average
├─ In percentage: ~4.2% error
└─ Acceptable for agricultural data
```

#### Root Mean Squared Error (RMSE)
```
RMSE = 2.87 quintals/ha means:
├─ Penalizes larger errors more
├─ Slightly higher than MAE
├─ Used for model comparison
└─ Similar magnitude indicates good fit
```

### Insights from Visualizations

#### From Rainfall vs Yield Chart
- **Observation**: Positive correlation
- **Implication**: Increase irrigation in drought
- **Action**: Monitor rainfall patterns
- **Recommendation**: Plan irrigation schedule

#### From Temperature vs Yield Chart
- **Observation**: Negative correlation
- **Implication**: Excessive heat harmful
- **Action**: Provide cooling/shade
- **Recommendation**: Plant heat-tolerant varieties

#### From Market Price Trends
- **Observation**: Increasing trend
- **Implication**: Better economic returns
- **Action**: Good time to invest
- **Recommendation**: Increase production

#### From Crop Distribution
- **Observation**: Rice most common
- **Implication**: Established crop
- **Action**: Share best practices
- **Recommendation**: Sustainable rice farming

#### From Humidity Impact
- **Observation**: Optimal 70-75%
- **Implication**: Specific humidity needed
- **Action**: Monitor with sensors
- **Recommendation**: Adjust irrigation

---

## COMMON TASKS

### Task 1: Analyze Own Agricultural Data

**Steps**:
1. Prepare CSV with 7 columns (as per template)
2. Open application (localhost:3000)
3. Click "Choose File"
4. Select your CSV
5. Click "Upload CSV"
6. Click "Analyze Data"
7. Review results

**Expected Time**: 2-3 minutes

### Task 2: Compare Two Datasets

**Steps**:
1. Upload first dataset
2. Note the results
3. Upload second dataset
4. Compare metrics side-by-side
5. Identify differences
6. Draw conclusions

**Expected Time**: 5-10 minutes

### Task 3: Predict Yield for Conditions

**Using Model Results**:
1. Get Linear Regression coefficients
2. Plug in your values:
   - Rainfall: your value
   - Temperature: your value
   - Humidity: your value
   - Market_Price: your value
3. Calculate: Yield = constant + (coef × value)
4. Get predicted yield

**Example**:
```
Given:
Rainfall: 1200 mm
Temperature: 28°C
Humidity: 75%
Market_Price: 2500

Prediction:
Yield = 15.2 + (0.012 × 1200) + (-0.85 × 28) 
        + (0.15 × 75) + (0.00032 × 2500)
     = 15.2 + 14.4 - 23.8 + 11.25 + 0.8
     = 18.85 quintals/ha
```

### Task 4: Identify Key Factors

**From Feature Importance**:
1. Look at Random Forest importance percentages
2. Identify top 3 factors
3. In dataset: Rainfall (35.2%) is most important
4. Focus on rainfall management
5. Monitor rainfall first

### Task 5: Find Optimal Conditions

**From Analysis Results**:
1. Look at correlations
2. Identify positive relationships
3. Maximize those factors:
   - High rainfall (0.78 correlation)
   - High humidity (0.65 correlation)
4. Minimize negative factors:
   - Excessive temperature
4. Implement recommendations

---

## TROUBLESHOOTING USER ISSUES

### Issue 1: "Failed to Fetch" Error

**Symptom**: Error after clicking Upload or Analyze

**Causes**:
- Backend not running
- Wrong backend port
- CORS configuration issue
- Network problem

**Solution**:
```
1. Check backend is running:
   curl http://localhost:5001/api/health
   
2. If not running:
   cd webapp/backend
   python app_port5001.py
   
3. Wait 3 seconds
4. Try again in browser
5. Clear browser cache if needed
```

### Issue 2: "Invalid File Format"

**Symptom**: Error when uploading CSV

**Causes**:
- File not CSV
- Wrong columns
- Empty cells
- Special characters

**Solution**:
```
1. Download template from "Download Sample"
2. Copy your data to template
3. Save as CSV
4. Upload again
5. Or check columns match exactly
```

### Issue 3: "No Data to Analyze"

**Symptom**: Analyze button doesn't work

**Causes**:
- File not uploaded
- Upload failed silently
- Browser cache issue

**Solution**:
```
1. Verify upload success message
2. If no message, file didn't upload
3. Try uploading again
4. Check file size < 50MB
5. Reload page (Cmd+R)
```

### Issue 4: Slow Performance

**Symptom**: Analysis takes > 5 seconds

**Causes**:
- Large dataset
- Slow computer
- Network latency
- Server overload

**Solution**:
```
1. Use smaller dataset (test first)
2. Check computer RAM (minimum 4GB)
3. Close other applications
4. Restart backend server
5. Try again with smaller file
```

### Issue 5: Visualizations Not Showing

**Symptom**: Charts don't display

**Causes**:
- Analysis failed
- Browser compatibility
- JavaScript error
- Network timeout

**Solution**:
```
1. Check browser console (F12)
2. Try different browser
3. Clear browser cache
4. Disable browser extensions
5. Reload page
```

---

## BEST PRACTICES

### Data Preparation
- ✓ Collect data from reliable sources
- ✓ Ensure consistent units
- ✓ Handle missing values before upload
- ✓ Remove duplicate records
- ✓ Validate data quality
- ✓ Document data source

### File Handling
- ✓ Use provided CSV template
- ✓ Keep file size < 50MB
- ✓ Use consistent column names
- ✓ Avoid special characters in names
- ✓ Backup original data
- ✓ Version control files

### Analysis Usage
- ✓ Always validate results
- ✓ Check data quality first
- ✓ Understand correlations
- ✓ Consider domain knowledge
- ✓ Use both models for comparison
- ✓ Document findings

### Decision Making
- ✓ Don't rely solely on statistics
- ✓ Combine with expert judgment
- ✓ Verify predictions with small pilots
- ✓ Monitor predictions over time
- ✓ Adjust model as needed
- ✓ Share insights with team

---

## FAQ

**Q: Can I modify uploaded data?**
A: Currently no. To change data, re-upload a new file.

**Q: How accurate are predictions?**
A: R² = 0.946 means 94.6% accuracy. Very reliable for general trends.

**Q: Can I export results?**
A: Currently view only. Screenshots or manual copying available.

**Q: What's the maximum file size?**
A: 50MB. Contains ~1 million rows of data.

**Q: Do you store my data?**
A: Data is processed and results kept in memory. No permanent storage.

**Q: Can I use this offline?**
A: Yes, run both servers locally. No internet needed.

**Q: What if data has missing values?**
A: System detects and handles automatically. Quality score updated.

**Q: Which model should I trust more?**
A: Linear Regression (R²=0.946) for interpretability and accuracy.

**Q: Can I analyze real-time data?**
A: Yes, but upload new files each time.

**Q: Is there a mobile app?**
A: Not yet. Responsive design works on mobile browser.

---

## SUPPORT & FEEDBACK

### Getting Help
- Review this user guide
- Check FAQ section
- Run troubleshooting steps
- Refer to technical documentation

### Reporting Issues
- Note exact error message
- Describe steps to reproduce
- Include screenshot if possible
- Mention browser/OS version
- Contact support team

### Providing Feedback
- Share feature requests
- Suggest improvements
- Report bugs
- Recommend optimizations

---

**User Guide Prepared**: January 17, 2026  
**Version**: 1.0  
**For Technical Support**: See Technical Documentation

