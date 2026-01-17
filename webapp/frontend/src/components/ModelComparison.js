import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line } from 'recharts';

function ModelComparison({ models }) {
  // Check if analysis contains model information (nested within analysis object)
  let modelResults = null;
  
  // Handle both direct models and nested analysis.models
  if (models.models) {
    modelResults = models.models;
  }

  if (!modelResults) {
    return null;
  }

  const lr = modelResults.linear_regression || {};
  const rf = modelResults.random_forest || {};

  // Prepare comparison data
  const comparisonData = [
    {
      metric: 'R² Score',
      'Linear Regression': (lr.r2_score * 100).toFixed(2),
      'Random Forest': (rf.r2_score * 100).toFixed(2),
    },
    {
      metric: 'MAE',
      'Linear Regression': lr.mae ? lr.mae.toFixed(2) : 0,
      'Random Forest': rf.mae ? rf.mae.toFixed(2) : 0,
    },
    {
      metric: 'RMSE',
      'Linear Regression': lr.rmse ? lr.rmse.toFixed(2) : 0,
      'Random Forest': rf.rmse ? rf.rmse.toFixed(2) : 0,
    },
  ];

  return (
    <div className="model-comparison">
      <h2>🤖 ML Model Comparison</h2>

      <div className="models-grid">
        {/* Linear Regression */}
        <div className="model-card">
          <h3>Linear Regression</h3>
          <div className="metrics">
            <div className="metric">
              <span>R² Score:</span>
              <strong>{(lr.r2_score * 100).toFixed(2)}%</strong>
            </div>
            <div className="metric">
              <span>MAE:</span>
              <strong>{lr.mae ? lr.mae.toFixed(2) : 'N/A'}</strong>
            </div>
            <div className="metric">
              <span>RMSE:</span>
              <strong>{lr.rmse ? lr.rmse.toFixed(2) : 'N/A'}</strong>
            </div>
            {lr.coefficients && (
              <div className="coefficients">
                <p><strong>Coefficients:</strong></p>
                {Object.keys(lr.coefficients).map((key) => (
                  <p key={key}>
                    {key}: {lr.coefficients[key].toFixed(4)}
                  </p>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Random Forest */}
        <div className="model-card best">
          <h3>Random Forest ⭐</h3>
          <div className="metrics">
            <div className="metric">
              <span>R² Score:</span>
              <strong>{(rf.r2_score * 100).toFixed(2)}%</strong>
            </div>
            <div className="metric">
              <span>MAE:</span>
              <strong>{rf.mae ? rf.mae.toFixed(2) : 'N/A'}</strong>
            </div>
            <div className="metric">
              <span>RMSE:</span>
              <strong>{rf.rmse ? rf.rmse.toFixed(2) : 'N/A'}</strong>
            </div>
            <p className="note">100 decision trees, max depth: 10</p>
          </div>
        </div>
      </div>

      {/* Comparison Chart */}
      <div className="comparison-chart">
        <h3>Metrics Comparison</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={comparisonData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="metric" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="Linear Regression" fill="#3498db" />
            <Bar dataKey="Random Forest" fill="#e74c3c" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Winner */}
      <div className="winner-box">
        <h3>🏆 Best Model</h3>
        <p>
          {rf.r2_score > lr.r2_score
            ? 'Random Forest performs better with higher R² score'
            : 'Linear Regression is more efficient'}
        </p>
        <p>Improvement: {((rf.r2_score / lr.r2_score - 1) * 100).toFixed(1)}% better R² score</p>
      </div>
    </div>
  );
}

export default ModelComparison;
