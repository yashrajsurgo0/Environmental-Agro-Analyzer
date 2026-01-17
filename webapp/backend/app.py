"""
Agricultural Data Analysis Backend
Flask API for data upload, processing, ML analysis, and visualization
"""
import os
import json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Global dataframe (for demo purposes)
current_df = None
analysis_results = None


# ==================== UTILITY FUNCTIONS ====================

def validate_csv(df):
    """Validate that CSV has required columns"""
    required_columns = ['Year', 'Crop', 'Rainfall_mm', 'Avg_Temperature_C', 'Crop_Yield', 'Market_Price']
    missing = [col for col in required_columns if col not in df.columns]
    return missing


def clean_data(df):
    """Clean and preprocess data"""
    df_clean = df.copy()
    
    # Handle missing values
    df_clean = df_clean.dropna()
    
    # Remove outliers using IQR method
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        df_clean = df_clean[(df_clean[col] >= Q1 - 1.5*IQR) & (df_clean[col] <= Q3 + 1.5*IQR)]
    
    return df_clean


def analyze_data(df):
    """Perform complete data analysis"""
    results = {}
    
    # Descriptive statistics
    results['descriptive_stats'] = df.describe().to_dict()
    results['shape'] = {'rows': df.shape[0], 'columns': df.shape[1]}
    
    # Correlations
    numeric_df = df.select_dtypes(include=[np.number])
    correlations = numeric_df.corr()
    results['correlations'] = correlations.to_dict()
    
    # Correlation with Crop_Yield
    if 'Crop_Yield' in numeric_df.columns:
        yield_corr = numeric_df.corr()['Crop_Yield'].sort_values(ascending=False)
        results['yield_correlations'] = yield_corr.to_dict()
    
    return results


def train_models(df):
    """Train ML models and return results"""
    # Prepare data
    feature_cols = ['Rainfall_mm', 'Avg_Temperature_C']
    if 'Humidity_Percent' in df.columns:
        feature_cols.append('Humidity_Percent')
    
    X = df[feature_cols].fillna(df[feature_cols].mean())
    y = df['Crop_Yield'].fillna(df['Crop_Yield'].mean())
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    results = {'models': {}, 'feature_importance': {}}
    
    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)
    y_pred_lr = lr.predict(X_test_scaled)
    
    results['models']['linear_regression'] = {
        'r2_score': float(r2_score(y_test, y_pred_lr)),
        'mae': float(mean_absolute_error(y_test, y_pred_lr)),
        'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred_lr))),
        'coefficients': dict(zip(feature_cols, lr.coef_.tolist()))
    }
    
    # Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    rf.fit(X_train_scaled, y_train)
    y_pred_rf = rf.predict(X_test_scaled)
    
    results['models']['random_forest'] = {
        'r2_score': float(r2_score(y_test, y_pred_rf)),
        'mae': float(mean_absolute_error(y_test, y_pred_rf)),
        'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred_rf)))
    }
    
    # Feature importance
    results['feature_importance']['random_forest'] = dict(zip(feature_cols, rf.feature_importances_.tolist()))
    
    # Store predictions for visualization
    results['predictions'] = {
        'linear_regression': y_pred_lr.tolist(),
        'random_forest': y_pred_rf.tolist(),
        'actual': y_test.tolist(),
        'test_indices': X_test.index.tolist()
    }
    
    return results


def generate_visualizations(df, analysis, models):
    """Generate data for visualizations"""
    viz_data = {}
    
    # Rainfall over time
    rainfall_by_year = df.groupby('Year')['Rainfall_mm'].mean().reset_index()
    viz_data['rainfall_trend'] = {
        'years': rainfall_by_year['Year'].tolist(),
        'values': rainfall_by_year['Rainfall_mm'].tolist()
    }
    
    # Temperature over time
    temp_by_year = df.groupby('Year')['Avg_Temperature_C'].mean().reset_index()
    viz_data['temperature_trend'] = {
        'years': temp_by_year['Year'].tolist(),
        'values': temp_by_year['Avg_Temperature_C'].tolist()
    }
    
    # Rainfall vs Crop Yield (scatter)
    viz_data['rainfall_vs_yield'] = {
        'x': df['Rainfall_mm'].tolist(),
        'y': df['Crop_Yield'].tolist(),
        'labels': df['Crop'].tolist()
    }
    
    # Temperature vs Crop Yield (scatter)
    viz_data['temperature_vs_yield'] = {
        'x': df['Avg_Temperature_C'].tolist(),
        'y': df['Crop_Yield'].tolist(),
        'labels': df['Crop'].tolist()
    }
    
    # Crop Yield vs Market Price
    viz_data['yield_vs_price'] = {
        'x': df['Crop_Yield'].tolist(),
        'y': df['Market_Price'].tolist(),
        'labels': df['Crop'].tolist()
    }
    
    # Crop-wise statistics
    crop_stats = df.groupby('Crop')[['Crop_Yield', 'Market_Price', 'Rainfall_mm']].mean()
    viz_data['crop_statistics'] = {
        'crops': crop_stats.index.tolist(),
        'yields': crop_stats['Crop_Yield'].tolist(),
        'prices': crop_stats['Market_Price'].tolist(),
        'rainfall': crop_stats['Rainfall_mm'].tolist()
    }
    
    # Feature importance
    if 'feature_importance' in models and 'random_forest' in models['feature_importance']:
        importance = models['feature_importance']['random_forest']
        viz_data['feature_importance'] = {
            'features': list(importance.keys()),
            'importance': list(importance.values())
        }
    
    # Model comparison
    viz_data['model_comparison'] = {
        'models': ['Linear Regression', 'Random Forest'],
        'r2_scores': [
            models['models']['linear_regression']['r2_score'],
            models['models']['random_forest']['r2_score']
        ],
        'mae': [
            models['models']['linear_regression']['mae'],
            models['models']['random_forest']['mae']
        ],
        'rmse': [
            models['models']['linear_regression']['rmse'],
            models['models']['random_forest']['rmse']
        ]
    }
    
    return viz_data


# ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Upload and process CSV file"""
    global current_df, analysis_results
    
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'Only CSV files are allowed'}), 400
        
        # Save and read file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Read CSV
        df = pd.read_csv(filepath)
        
        # Validate
        missing_cols = validate_csv(df)
        if missing_cols:
            return jsonify({
                'error': f'Missing required columns: {", ".join(missing_cols)}',
                'required_columns': ['Year', 'Crop', 'Rainfall_mm', 'Avg_Temperature_C', 'Crop_Yield', 'Market_Price']
            }), 400
        
        # Store dataframe
        current_df = df.copy()
        
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': file.filename,
            'rows': df.shape[0],
            'columns': df.shape[1],
            'columns_list': df.columns.tolist()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze uploaded data"""
    global current_df, analysis_results
    
    try:
        if current_df is None or current_df.empty:
            return jsonify({'error': 'No data uploaded yet'}), 400
        
        # Clean data
        df_clean = clean_data(current_df)
        
        # Analyze
        analysis = analyze_data(df_clean)
        
        # Train models
        models = train_models(df_clean)
        
        # Generate visualizations
        viz_data = generate_visualizations(df_clean, analysis, models)
        
        # Store results
        analysis_results = {
            'analysis': analysis,
            'models': models,
            'visualizations': viz_data
        }
        
        return jsonify({
            'message': 'Analysis completed successfully',
            'analysis': analysis,
            'models': models,
            'visualizations': viz_data
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/results', methods=['GET'])
def get_results():
    """Get analysis results"""
    global analysis_results
    
    if analysis_results is None:
        return jsonify({'error': 'No analysis results available'}), 400
    
    return jsonify(analysis_results), 200


@app.route('/api/download-sample', methods=['GET'])
def download_sample():
    """Get sample data template"""
    sample_data = {
        'Year': [2019, 2019, 2020],
        'Crop': ['Wheat', 'Rice', 'Corn'],
        'Rainfall_mm': [450.5, 850.3, 650.2],
        'Avg_Temperature_C': [18.2, 22.5, 20.1],
        'Crop_Yield': [2850, 4200, 3800],
        'Market_Price': [250.50, 180.75, 220.00]
    }
    return jsonify({
        'message': 'Sample CSV template',
        'columns': list(sample_data.keys()),
        'sample': sample_data,
        'csv_header': ','.join(sample_data.keys()),
        'csv_sample': '\n'.join([
            'Year,Crop,Rainfall_mm,Avg_Temperature_C,Crop_Yield,Market_Price',
            '2019,Wheat,450.5,18.2,2850,250.50',
            '2019,Rice,850.3,22.5,4200,180.75',
            '2020,Corn,650.2,20.1,3800,220.00'
        ])
    }), 200


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get current data statistics"""
    global current_df
    
    if current_df is None or current_df.empty:
        return jsonify({'error': 'No data available'}), 400
    
    return jsonify({
        'rows': current_df.shape[0],
        'columns': current_df.shape[1],
        'columns_list': current_df.columns.tolist(),
        'dtypes': current_df.dtypes.to_dict(),
        'missing_values': current_df.isnull().sum().to_dict()
    }), 200


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Agricultural Data Analysis Backend")
    print("="*60)
    print("\n📊 API Documentation:")
    print("  POST   /api/upload     - Upload CSV file")
    print("  POST   /api/analyze    - Analyze data & train models")
    print("  GET    /api/results    - Get analysis results")
    print("  GET    /api/stats      - Get data statistics")
    print("  GET    /api/download-sample - Get sample template")
    print("\n🔗 Server: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
