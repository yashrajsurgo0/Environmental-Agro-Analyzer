# ENVIRONMENTAL AGRO ANALYZER
## Installation & Deployment Guide

**Document Type**: Installation Manual  
**Version**: 1.0  
**Date**: January 17, 2026

---

## INSTALLATION OVERVIEW

### System Requirements

**Hardware**:
- CPU: 2+ cores (Intel/AMD)
- RAM: 4GB minimum (8GB recommended)
- Storage: 2GB free space
- Network: Internet for initial setup

**Operating System**:
- macOS 10.14+
- Ubuntu 18.04 LTS+
- Windows 10/11
- Any system with Python 3.10+

**Software**:
- Python: 3.10 or higher (tested with 3.13.7)
- Node.js: 14 or higher (tested with v18+)
- npm: 6 or higher
- Git: Optional (for version control)

### Supported Environments

| Environment | Status | Notes |
|-------------|--------|-------|
| macOS (Intel) | ✅ | Tested & Verified |
| macOS (Apple Silicon) | ✅ | Tested & Verified |
| Ubuntu 20.04+ | ✅ | Should work |
| Windows 10/11 | ✅ | Use WSL2 recommended |
| Raspberry Pi | ⚠️ | Limited resources |
| Docker | 🔄 | Planned (Phase 2) |

---

## STEP-BY-STEP INSTALLATION

### Step 1: Download & Setup Project

#### macOS/Linux

```bash
# Navigate to project directory
cd /Users/yashrajsurgoniwar/Desktop/PROJECT

# Verify project structure
ls -la

# Expected output:
# webapp/
# maharashtra_agricultural_data.csv
# Climate_Agricultural_Markets.ipynb
# ... (other files)
```

#### Windows

```powershell
# Navigate to project
cd C:\Users\YourUsername\Desktop\PROJECT

# Verify structure
dir

# Expected: webapp folder, CSV file, etc.
```

---

### Step 2: Setup Python Environment

#### macOS/Linux

```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Verify activation
which python  # Should show .venv path
python --version  # Should show 3.10+
```

#### Windows

```powershell
# Create virtual environment
python -m venv .venv

# Activate environment
.venv\Scripts\activate

# Verify (command prompt should show (.venv) prefix)
python --version
```

**Troubleshooting Python**:
```bash
# If python command not found
python3 --version

# If Python 3.10+ not installed
# Download from: https://www.python.org/downloads/

# Verify installation
python -m venv --help  # Should show help
```

---

### Step 3: Install Python Dependencies

#### Option A: Using requirements.txt (Recommended)

```bash
# Ensure venv is activated
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Navigate to backend
cd webapp/backend

# Install all dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

#### Option B: Manual Installation

```bash
# Activate venv first
source .venv/bin/activate

# Install packages individually
pip install Flask==3.1.2
pip install Flask-CORS==6.0.2
pip install pandas==2.3.3
pip install numpy==2.4.1
pip install scikit-learn==1.8.0
pip install matplotlib==3.10.8
pip install seaborn==0.13.2

# Verify
python -c "import flask; print(flask.__version__)"
```

**Expected Output**:
```
Successfully installed Flask-3.1.2
Successfully installed Flask-CORS-6.0.2
Successfully installed pandas-2.3.3
... (7 packages total)
```

---

### Step 4: Verify Backend Setup

```bash
# Test Python imports
python -c "import pandas, sklearn, flask; print('✓ All imports successful')"

# Expected output:
# ✓ All imports successful

# Check Flask app syntax
python -m py_compile app_port5001.py

# Expected output:
# (no output = success)
```

---

### Step 5: Install Node.js (If Not Already Installed)

#### Check Installation

```bash
node --version  # Should show v14+
npm --version   # Should show 6+
```

#### Install Node.js

**macOS with Homebrew**:
```bash
# Check brew availability
brew --version

# If not installed, install Homebrew first:
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node

# Verify
node --version
npm --version
```

**Alternative: Direct Download**:
```bash
# Download from: https://nodejs.org/
# Choose LTS version (16+)
# Run installer and follow prompts
# Verify: node --version
```

**Windows**:
```powershell
# Download: https://nodejs.org/
# Run installer
# Add to PATH (done by installer)
# Verify: node --version
```

---

### Step 6: Setup Frontend

```bash
# Navigate to frontend
cd webapp/frontend

# Install Node dependencies
npm install

# Expected: 1300+ packages installed, ~5 minutes

# Install Recharts for visualizations
npm install recharts

# Verify
npm list recharts
```

**Troubleshooting npm**:
```bash
# If npm not found
eval "$(/opt/homebrew/bin/brew shellenv)"  # Add brew to PATH

# If slow installation
npm config set registry https://registry.npmjs.org/

# Clear npm cache if issues
npm cache clean --force
```

---

## STARTING SERVICES

### Terminal Setup

You'll need 2 terminals:
- **Terminal 1**: Backend (Flask)
- **Terminal 2**: Frontend (React)

---

### Starting Backend Server

#### Terminal 1 - Backend

```bash
# Navigate to project
cd /Users/yashrajsurgoniwar/Desktop/PROJECT

# Activate Python environment
source .venv/bin/activate

# Navigate to backend
cd webapp/backend

# Start server
python app_port5001.py

# Expected output:
# ============================================================
# 🚀 Agricultural Data Analysis Backend
# ============================================================
# 
# 📊 API Documentation:
#   POST   /api/upload     - Upload CSV file
#   POST   /api/analyze    - Analyze data & train models
#   GET    /api/results    - Get analysis results
#   GET    /api/stats      - Get data statistics
#   GET    /api/download-sample - Get sample template
# 
# 🔗 Server: http://localhost:5001
# ============================================================
# 
# 📁 Loading real Maharashtra data...
# ✅ Loaded 50 records successfully!
# ✅ Pre-loaded analysis complete!
# 
# Model Performance:
#   Linear Regression R²: 0.946
#   Random Forest R²: 0.932
# 
#  * Running on http://127.0.0.1:5001
#  * Press CTRL+C to quit
```

**Verification**:
```bash
# In another terminal, test backend
curl http://localhost:5001/api/health

# Expected response:
# {"status":"healthy","version":"1.0"}
```

---

### Starting Frontend Server

#### Terminal 2 - Frontend

```bash
# Ensure brew in PATH (macOS)
eval "$(/opt/homebrew/bin/brew shellenv)"

# Navigate to frontend
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/frontend

# Start React development server
npm start

# Expected output:
# ...
# Compiled successfully!
# 
# You can now view agricultural-analysis-frontend in the browser.
# 
#   Local:            http://localhost:3000
#   On Your Network:  http://172.20.10.2:3000
# 
# Note that the development build is not optimized.
# To create a production build, use npm run build.
# 
# webpack compiled successfully
```

---

### Step 7: Open Application

**In Your Browser**:
```
Type: http://localhost:3000
Press: Enter
```

**Expected**:
- Application loads
- Upload interface visible
- "🌾 Agricultural Data Analysis Platform" header
- "📤 Upload Agricultural Data" section ready

---

## VERIFICATION CHECKLIST

### ✓ Backend Verification

```bash
# Test 1: Health Check
curl http://localhost:5001/api/health
# Should return: {"status":"healthy",...}

# Test 2: API Documentation
curl http://localhost:5001/
# Should display: API endpoints list

# Test 3: Download Sample
curl http://localhost:5001/api/download-sample -o test.csv
# Should download: CSV file

# Test 4: Statistics
curl http://localhost:5001/api/stats
# Should return: {"status":"success", "total_records":50,...}
```

### ✓ Frontend Verification

```bash
# Check 1: Page loads
# http://localhost:3000 should display the platform

# Check 2: Console clean
# F12 → Console tab should have no errors

# Check 3: File upload ready
# Upload button should be clickable and enabled

# Check 4: Responsive
# Resize browser - layout should adjust smoothly
```

### ✓ Integration Verification

```bash
# Test 1: Upload sample data
# 1. Click "Choose File"
# 2. Select sample CSV
# 3. Click "Upload CSV"
# 4. Should see: "✓ File uploaded"

# Test 2: Analyze data
# 1. Click "📊 Analyze Data"
# 2. Wait 1-2 seconds
# 3. Should see: Statistics & results

# Test 3: View visualizations
# 1. Scroll down after analysis
# 2. Should see: 8 charts
# 3. Charts should be interactive

# Test 4: Check console
# F12 → Network tab
# Should see: Successful API calls
```

---

## TROUBLESHOOTING

### Issue 1: "Address Already in Use" (Port 5000)

**Error Message**:
```
OSError: [Errno 98] Address already in use
```

**Solution**:
```bash
# Option 1: Kill process on port 5000
lsof -ti:5000 | xargs kill -9
# Then restart: python app_port5001.py

# Option 2: Use different port
# Edit app_port5001.py, line 670:
# Change: port=5001 to port=5002

# Option 3: Disable AirPlay (macOS)
# System Preferences > Sound > AirPlay > Uncheck
```

---

### Issue 2: "ModuleNotFoundError: flask"

**Error Message**:
```
ModuleNotFoundError: No module named 'flask'
```

**Solution**:
```bash
# Verify virtual environment is activated
source .venv/bin/activate
# Check if (.venv) appears in terminal

# Install dependencies
pip install -r requirements.txt

# Verify Flask installed
python -c "import flask; print(flask.__version__)"
```

---

### Issue 3: "npm: command not found"

**Error Message**:
```
zsh: command not found: npm
```

**Solution**:
```bash
# Add Homebrew to PATH
eval "$(/opt/homebrew/bin/brew shellenv)"

# Verify Node.js installed
node --version

# If not installed
brew install node

# Try npm again
npm --version
```

---

### Issue 4: "CORS Error" in Browser

**Browser Console Error**:
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solution**:
```
1. Ensure backend running on port 5001
2. Check frontend calls use http://localhost:5001
3. Verify Flask-CORS installed: pip show flask-cors
4. Restart both servers
5. Clear browser cache (Ctrl+Shift+Del)
```

---

### Issue 5: "CSV Upload Failed"

**Error in Frontend**:
```
Upload failed or File validation error
```

**Solution**:
1. Check file is .csv format (not .xlsx)
2. Verify all 7 columns present:
   - Year, Crop, Rainfall_mm, Avg_Temperature_C
   - Crop_Yield, Market_Price, Humidity_Percent
3. Ensure no empty cells
4. File size < 50MB
5. Use provided template: Download Sample button

---

### Issue 6: Slow Performance

**Symptoms**: Analysis takes > 10 seconds

**Solution**:
```bash
# 1. Check system resources
top  # Or Activity Monitor (macOS)
# Should see available RAM

# 2. Restart services
# Kill both backend and frontend
# Restart in order: Backend first, then Frontend

# 3. Test with smaller dataset
# Use subset of data for testing

# 4. Check network
# curl http://localhost:5001/api/health
# Should be < 100ms
```

---

### Issue 7: Charts Not Showing

**Symptoms**: Analysis completes but no visualizations

**Solution**:
```bash
# 1. Check browser console
F12 → Console tab for errors

# 2. Try different browser
Chrome, Firefox, Safari all work

# 3. Clear cache
Ctrl+Shift+Del (Windows) or Cmd+Shift+Del (macOS)

# 4. Check Recharts installed
cd frontend
npm list recharts
# Should show version 2.10+

# 5. Restart frontend
npm start
```

---

## PRODUCTION DEPLOYMENT

### Pre-Production Checklist

```
✓ All tests passed
✓ Error handling tested
✓ Performance acceptable
✓ Documentation complete
✓ Security reviewed
✓ Backup strategy defined
✓ Monitoring configured
✓ Support procedures established
```

### Using Gunicorn (Production WSGI)

```bash
# Install Gunicorn
pip install gunicorn

# Run backend with Gunicorn
cd webapp/backend
gunicorn --bind 0.0.0.0:5001 app_port5001:app

# With multiple workers (more requests)
gunicorn --bind 0.0.0.0:5001 --workers 4 app_port5001:app

# With specific timeout
gunicorn --bind 0.0.0.0:5001 --timeout 120 app_port5001:app
```

### Using PM2 (Process Manager)

```bash
# Install PM2
npm install -g pm2

# Start backend
pm2 start --name "agro-backend" python -- webapp/backend/app_port5001.py

# Start frontend
pm2 start --name "agro-frontend" npm -- --prefix webapp/frontend start

# Monitor
pm2 monit

# View logs
pm2 logs agro-backend
pm2 logs agro-frontend
```

### Docker Deployment (Future)

```dockerfile
# Dockerfile for backend
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app_port5001:app"]
```

```bash
# Build image
docker build -t agro-analyzer-backend .

# Run container
docker run -p 5001:5001 agro-analyzer-backend
```

---

## MAINTENANCE

### Regular Maintenance Tasks

**Daily**:
```bash
# Check services running
curl http://localhost:5001/api/health
curl http://localhost:3000

# Review error logs
tail -f backend.log (if logging configured)
```

**Weekly**:
```bash
# Update dependencies
pip install --upgrade pip
npm update

# Backup data
cp maharashtra_agricultural_data.csv \
   maharashtra_agricultural_data.backup.csv

# Test backup restore
# Restore from backup if needed
```

**Monthly**:
```bash
# Full dependency audit
pip audit
npm audit

# Performance analysis
# Monitor response times
# Check disk usage

# Database maintenance
# If database added in Phase 2
# Run optimization queries
```

### Backup Strategy

```bash
# Backup project files
tar -czf agro-analyzer-backup-$(date +%Y%m%d).tar.gz \
    webapp/backend \
    webapp/frontend \
    maharashtra_agricultural_data.csv

# Backup to external drive
cp agro-analyzer-backup-*.tar.gz /Volumes/Backup/

# Automated daily backup (cron)
0 2 * * * cd /path/to/project && \
  tar -czf backup-$(date +\%Y\%m\%d).tar.gz . && \
  cp backup-*.tar.gz /backup/location/
```

### Update Dependencies

```bash
# Check outdated packages
pip list --outdated
npm outdated

# Update specific package
pip install --upgrade Flask
npm update recharts

# Update all packages
pip install --upgrade pip
npm update

# Clean old versions
pip cache purge
npm cache clean --force
```

---

## PERFORMANCE OPTIMIZATION

### Backend Optimization

```python
# Enable caching (future update)
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/results')
@cache.cached(timeout=300)  # Cache for 5 minutes
def get_results():
    return cached_results
```

### Frontend Optimization

```javascript
// Code splitting
import React, { lazy, Suspense } from 'react';

const Visualizations = lazy(() => import('./Visualizations'));

// Lazy loading in component
<Suspense fallback={<div>Loading...</div>}>
  <Visualizations data={vizData} />
</Suspense>
```

### Database Query Optimization (Phase 2)

```sql
-- Add indexes for common queries
CREATE INDEX idx_year ON agricultural_data(year);
CREATE INDEX idx_crop ON agricultural_data(crop);
CREATE INDEX idx_year_crop ON agricultural_data(year, crop);
```

---

## MONITORING & LOGGING

### Enable Logging

```python
# Add to app_port5001.py
import logging

logging.basicConfig(
    filename='backend.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    logger.info(f"File upload started")
    try:
        # ... upload logic
        logger.info(f"File uploaded successfully")
    except Exception as e:
        logger.error(f"Upload failed: {e}")
```

### View Logs

```bash
# Real-time log monitoring
tail -f backend.log

# Last 50 lines
tail -50 backend.log

# Search logs
grep "error" backend.log

# Count errors
grep -c "ERROR" backend.log
```

---

## SUPPORT & DOCUMENTATION

### Getting Help

```
1. Check this guide
2. Review troubleshooting section
3. Check API documentation
4. Review code comments
5. Check browser console for errors
```

### Useful Resources

- [Python Documentation](https://docs.python.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [npm Documentation](https://docs.npmjs.com/)
- [Recharts Examples](https://recharts.org/)

### Reporting Issues

Include in report:
1. Error message (exact text)
2. Steps to reproduce
3. Expected vs actual behavior
4. Screenshot if applicable
5. System information (OS, Python version)

---

## QUICK REFERENCE

### Command Cheat Sheet

```bash
# Start backend
cd webapp/backend && python app_port5001.py

# Start frontend
cd webapp/frontend && npm start

# Stop services
Ctrl+C in both terminals

# View backend logs
curl http://localhost:5001/api/health

# Test upload
curl -X POST -F "file=@sample.csv" http://localhost:5001/api/upload

# Activate venv
source .venv/bin/activate

# Deactivate venv
deactivate

# Install package
pip install package_name

# Uninstall package
pip uninstall package_name

# List installed packages
pip list

# Upgrade pip
pip install --upgrade pip
```

---

**Installation Guide Prepared**: January 17, 2026  
**Version**: 1.0  
**For Support**: Refer to documentation files

