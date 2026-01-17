import React from 'react';

function DataAnalysis({ analysis }) {
  const stats = analysis.descriptive_stats;

  return (
    <div className="data-analysis">
      <h2>📊 Data Analysis</h2>
      <div className="stats-grid">
        {stats && Object.keys(stats).map((feature) => (
          <div key={feature} className="stat-card">
            <h3>{feature}</h3>
            <div className="stat-values">
              {stats[feature].count && <p><strong>Count:</strong> {Math.round(stats[feature].count)}</p>}
              {stats[feature]['50%'] && <p><strong>Median:</strong> {stats[feature]['50%'].toFixed(2)}</p>}
              {stats[feature].mean && <p><strong>Mean:</strong> {stats[feature].mean.toFixed(2)}</p>}
              {stats[feature].std && <p><strong>Std Dev:</strong> {stats[feature].std.toFixed(2)}</p>}
              {stats[feature].min && <p><strong>Min:</strong> {stats[feature].min.toFixed(2)}</p>}
              {stats[feature].max && <p><strong>Max:</strong> {stats[feature].max.toFixed(2)}</p>}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DataAnalysis;
