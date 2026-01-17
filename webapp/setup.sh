#!/bin/bash

# Agricultural Data Analysis Platform - Complete Setup Script
# This script sets up both backend and frontend

echo "=========================================="
echo "🌾 Agricultural Data Analysis Platform"
echo "Complete Setup Script"
echo "=========================================="
echo ""

# Check if Node.js is installed
echo "📦 Checking Node.js..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    echo "   Download from: https://nodejs.org/"
    exit 1
fi
echo "✓ Node.js $(node --version) found"

# Check if Python is installed
echo ""
echo "📦 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3 first."
    exit 1
fi
echo "✓ Python $(python3 --version) found"

# Setup Backend
echo ""
echo "=========================================="
echo "⚙️  Setting up Backend..."
echo "=========================================="

cd webapp/backend

# Create virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "✓ Backend setup complete!"
echo ""

# Setup Frontend
echo "=========================================="
echo "⚙️  Setting up Frontend..."
echo "=========================================="

cd ../frontend

# Install Node dependencies
echo "Installing Node dependencies..."
npm install
npm install recharts

echo "✓ Frontend setup complete!"
echo ""

# Summary
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "📝 Next Steps:"
echo ""
echo "1. Start Backend (Terminal 1):"
echo "   cd webapp/backend"
echo "   source venv/bin/activate  # if using virtual env"
echo "   python app.py"
echo ""
echo "2. Start Frontend (Terminal 2):"
echo "   cd webapp/frontend"
echo "   npm start"
echo ""
echo "3. Open in browser:"
echo "   http://localhost:3000"
echo ""
echo "📊 API Server (Backend):"
echo "   http://localhost:5000"
echo ""
echo "=========================================="
