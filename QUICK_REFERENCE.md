# ⚡ QUICK REFERENCE GUIDE

## 🎯 START HERE

```bash
# Terminal 1: Start Backend
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/backend
python app.py

# Terminal 2: Start Frontend  
cd /Users/yashrajsurgoniwar/Desktop/PROJECT/webapp/frontend
npm start

# Browser
http://localhost:3000
```

---

## 📋 WHAT YOU HAVE

| Item | Location | Purpose |
|------|----------|---------|
| Real Data | `maharashtra_agricultural_data.csv` | 50 records from 2019-2023 |
| Notebook | `Climate_Agricultural_Markets.ipynb` | Jupyter analysis (updated!) |
| Backend API | `webapp/backend/app.py` | Flask server |
| Frontend UI | `webapp/frontend/App.js` | React interface |
| Documentation | `WEBAPP_SETUP_GUIDE.md` | Complete guide |

---

## 🚀 QUICK SETUP

### Option 1: One-line Setup (Mac/Linux)
```bash
cd /Users/yashrajsurgoniwar/Desktop/PROJECT
bash webapp/setup.sh
```

### Option 2: Manual Setup
```bash
# Backend
cd webapp/backend && pip install -r requirements.txt

# Frontend
cd ../frontend && npm install && npm install recharts
```

---

## 📊 USING THE APP

1. **Upload** → Select `maharashtra_agricultural_data.csv`
2. **Analyze** → Click "📊 Analyze Data"
3. **View** → See results and visualizations

---

## 🔧 USEFUL COMMANDS

```bash
# Backend
python app.py                    # Start server
curl http://localhost:5000/api/health   # Test API

# Frontend
npm start                        # Start dev server
npm run build                    # Build for production

# Notebook
jupyter notebook Climate_Agricultural_Markets.ipynb  # Run notebook
```

---

## 🐛 FIX COMMON ISSUES

### Port in use?
```bash
# Mac/Linux
lsof -ti:5000 | xargs kill -9
lsof -ti:3000 | xargs kill -9
```

### Module not found?
```bash
cd webapp/backend
pip install -r requirements.txt
```

### npm error?
```bash
cd webapp/frontend
npm cache clean --force
npm install
```

---

## 📁 FILES REFERENCE

```
PROJECT/
├── maharashtra_agricultural_data.csv     ← Real data (USE THIS!)
├── Climate_Agricultural_Markets.ipynb    ← Jupyter notebook
├── WEBAPP_SETUP_GUIDE.md                 ← Full setup guide
├── WEBAPP_README.md                      ← App documentation
└── webapp/
    ├── backend/app.py                    ← Flask API
    └── frontend/App.js                   ← React app
```

---

## 📊 API ENDPOINTS

```
GET  /api/health
POST /api/upload
POST /api/analyze
GET  /api/results
GET  /api/stats
GET  /api/download-sample
```

---

## ✅ VERIFICATION

After startup, check:
- ✅ Backend: `curl http://localhost:5000/api/health`
- ✅ Frontend: `http://localhost:3000` loads
- ✅ Can upload CSV
- ✅ Can analyze data
- ✅ Results display

---

## 📈 WHAT YOU CAN DO

- ✅ Upload agricultural CSV data
- ✅ View statistics & correlations
- ✅ Train ML models automatically
- ✅ See interactive visualizations
- ✅ Compare model performance
- ✅ Download results
- ✅ Use your own data

---

## 🎓 NEXT STEPS

1. **Start the app** (see Quick Start above)
2. **Upload included data** (maharashtra_agricultural_data.csv)
3. **Analyze** and view results
4. **Try your own data** (must have: Year, Crop, Rainfall_mm, Avg_Temperature_C, Crop_Yield, Market_Price)

---

## 📞 NEED HELP?

See full guides:
- **Setup**: `WEBAPP_SETUP_GUIDE.md`
- **API**: `WEBAPP_README.md`
- **Data**: `DATASET_EXPLANATION.md`
- **Summary**: `PROJECT_DELIVERY_SUMMARY.md`

---

**Ready? Start with:** `python app.py` + `npm start` 🚀
