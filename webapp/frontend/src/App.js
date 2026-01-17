import React, { useState } from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import DataAnalysis from './components/DataAnalysis';
import Visualizations from './components/Visualizations';
import ModelComparison from './components/ModelComparison';

function App() {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [analysisData, setAnalysisData] = useState(null);
  const [vizData, setVizData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileUpload = (filename) => {
    setUploadedFile(filename);
    setError(null);
  };

  const handleAnalyze = async () => {
    if (!uploadedFile) {
      setError('Please upload a file first');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:5001/api/analyze', {
        method: 'POST',
      });

      if (!response.ok) {
        throw new Error('Analysis failed');
      }

      const data = await response.json();
      setAnalysisData(data.analysis);
      setVizData(data.visualizations);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1>🌾 Agricultural Data Analysis Platform</h1>
        <p>Upload, Analyze, and Visualize Agricultural Climate Data with ML Models</p>
      </header>

      <div className="container">
        {error && <div className="error-message">{error}</div>}

        <div className="section">
          <FileUpload onFileUpload={handleFileUpload} />
        </div>

        {uploadedFile && (
          <>
            <div className="action-buttons">
              <button
                onClick={handleAnalyze}
                disabled={loading}
                className="analyze-button"
              >
                {loading ? '⏳ Analyzing...' : '📊 Analyze Data'}
              </button>
            </div>

            {loading && <div className="loading">Processing your data...</div>}

            {analysisData && (
              <>
                <DataAnalysis analysis={analysisData} />
                <ModelComparison models={analysisData} />
                {vizData && <Visualizations data={vizData} />}
              </>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default App;
