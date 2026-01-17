import React, { useState } from 'react';

function FileUpload({ onFileUpload }) {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [uploadMessage, setUploadMessage] = useState('');
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError('');
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file');
      return;
    }

    setUploading(true);
    setError('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5001/api/upload', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Upload failed');
      }

      setUploadMessage(`✓ File uploaded: ${data.filename} (${data.rows} rows)`);
      onFileUpload(data.filename);
      setFile(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="file-upload">
      <h2>📤 Upload Agricultural Data</h2>
      <div className="upload-area">
        <input
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          disabled={uploading}
        />
        <button
          onClick={handleUpload}
          disabled={uploading || !file}
          className="upload-button"
        >
          {uploading ? '⏳ Uploading...' : '📤 Upload CSV'}
        </button>
      </div>
      {uploadMessage && <p className="success">{uploadMessage}</p>}
      {error && <p className="error">{error}</p>}
      <div className="template-info">
        <p>📋 CSV should contain: Year, Crop, Rainfall_mm, Avg_Temperature_C, Crop_Yield, Market_Price</p>
      </div>
    </div>
  );
}

export default FileUpload;
