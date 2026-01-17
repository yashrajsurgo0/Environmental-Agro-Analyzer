import React from 'react';
import { LineChart, Line, BarChart, Bar, ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Visualizations({ data }) {
  // Rainfall trend data
  const rainfallData = data.rainfall_trend
    ? data.rainfall_trend.years.map((year, idx) => ({
        year,
        rainfall: data.rainfall_trend.values[idx],
      }))
    : [];

  // Temperature trend data
  const tempData = data.temperature_trend
    ? data.temperature_trend.years.map((year, idx) => ({
        year,
        temperature: data.temperature_trend.values[idx],
      }))
    : [];

  // Rainfall vs Yield
  const rainfallVsYieldData = data.rainfall_vs_yield
    ? data.rainfall_vs_yield.x.map((rainfall, idx) => ({
        rainfall: parseFloat(rainfall.toFixed(2)),
        yield: parseFloat(data.rainfall_vs_yield.y[idx].toFixed(2)),
        crop: data.rainfall_vs_yield.labels[idx],
      }))
    : [];

  // Crop statistics data
  const cropStatsData = data.crop_statistics
    ? data.crop_statistics.crops.map((crop, idx) => ({
        crop: crop.substring(0, 8),
        yield: data.crop_statistics.yields[idx],
        price: data.crop_statistics.prices[idx],
        rainfall: data.crop_statistics.rainfall[idx],
      }))
    : [];

  // Feature importance
  const featureImportanceData = data.feature_importance
    ? data.feature_importance.features.map((feature, idx) => ({
        feature,
        importance: data.feature_importance.importance[idx],
      }))
    : [];

  return (
    <div className="visualizations">
      <h2>📈 Visualizations</h2>

      <div className="viz-grid">
        {/* Rainfall Trend */}
        {rainfallData.length > 0 && (
          <div className="viz-card">
            <h3>Rainfall Over Time</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={rainfallData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="rainfall" stroke="#3498db" dot={{ fill: '#3498db', r: 4 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Temperature Trend */}
        {tempData.length > 0 && (
          <div className="viz-card">
            <h3>Temperature Over Time</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={tempData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="temperature" stroke="#e74c3c" dot={{ fill: '#e74c3c', r: 4 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Rainfall vs Yield */}
        {rainfallVsYieldData.length > 0 && (
          <div className="viz-card">
            <h3>Rainfall vs Crop Yield</h3>
            <ResponsiveContainer width="100%" height={300}>
              <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="rainfall" name="Rainfall (mm)" />
                <YAxis dataKey="yield" name="Crop Yield" />
                <Tooltip cursor={{ strokeDasharray: '3 3' }} />
                <Scatter data={rainfallVsYieldData} fill="#27ae60" />
              </ScatterChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Crop Statistics */}
        {cropStatsData.length > 0 && (
          <div className="viz-card">
            <h3>Crop-wise Average Yield</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={cropStatsData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="crop" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="yield" fill="#f39c12" name="Avg Yield" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* Feature Importance */}
        {featureImportanceData.length > 0 && (
          <div className="viz-card">
            <h3>Feature Importance (Random Forest)</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={featureImportanceData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="feature" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="importance" fill="#9b59b6" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>
    </div>
  );
}

export default Visualizations;
