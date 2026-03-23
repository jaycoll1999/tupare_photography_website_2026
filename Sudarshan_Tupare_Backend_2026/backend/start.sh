#!/bin/bash

echo "Starting Sudarshan Tupare Photography Backend API..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env file with your actual configuration values"
    read -p "Press Enter to continue after editing .env file..."
fi

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

# Start the server
echo "Starting FastAPI server..."
echo "API will be available at http://localhost:8000"
echo "Documentation available at http://localhost:8000/docs"
echo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
