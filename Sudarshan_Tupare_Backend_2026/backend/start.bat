@echo off
echo Starting Sudarshan Tupare Photography Backend API...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo Please edit .env file with your actual configuration values
    pause
)

REM Run database migrations
echo Running database migrations...
alembic upgrade head

REM Start the server
echo Starting FastAPI server...
echo API will be available at http://localhost:8000
echo Documentation available at http://localhost:8000/docs
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
