# Sudarshan Tupare Photography - Backend API

A production-ready FastAPI backend for the Sudarshan Tupare Photography website.

## Features

- **Authentication**: JWT-based admin authentication
- **Portfolio Management**: Image gallery with categories
- **Booking System**: Event booking management
- **Pricing Management**: Dynamic pricing packages
- **Testimonials**: Client testimonials management
- **Contact Forms**: Contact message handling
- **Image Upload**: Cloudinary integration for image storage
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Migrations**: Alembic for database versioning

## Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern, fast web framework
- **PostgreSQL** - Production database
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **JWT** - Authentication
- **Cloudinary** - Image storage
- **Pydantic** - Data validation

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── routes/              # API endpoints
│   ├── auth/                # Authentication logic
│   └── utils/               # Utility functions
├── alembic/                 # Database migrations
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## Setup Instructions

### 1. Prerequisites

- Python 3.11+
- PostgreSQL 12+
- Cloudinary account (for image storage)

### 2. Installation

```bash
# Clone the repository
git clone <repository-url>
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your actual values:
DATABASE_URL=postgresql://username:password@localhost:5432/sudarshan_photography
SECRET_KEY=your-super-secret-key-here
CLOUDINARY_NAME=your-cloudinary-cloud-name
CLOUDINARY_KEY=your-cloudinary-api-key
CLOUDINARY_SECRET=your-cloudinary-api-secret
```

### 4. Database Setup

```bash
# Create PostgreSQL database
createdb sudarshan_photography

# Run database migrations
alembic upgrade head

# Create initial admin user (optional - can be done via API)
```

### 5. Running the Application

```bash
# Start the development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or for production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /auth/login` - Admin login
- `POST /auth/register` - Register admin user

### Portfolio
- `GET /portfolio` - Get all portfolio images
- `POST /portfolio` - Add portfolio image (admin only)
- `PUT /portfolio/{id}` - Update portfolio image (admin only)
- `DELETE /portfolio/{id}` - Delete portfolio image (admin only)

### Bookings
- `POST /booking` - Create new booking
- `GET /booking` - Get all bookings (admin only)
- `PUT /booking/{id}` - Update booking status (admin only)

### Pricing
- `GET /pricing` - Get all pricing plans
- `POST /pricing` - Create pricing plan (admin only)
- `PUT /pricing/{id}` - Update pricing plan (admin only)

### Testimonials
- `GET /testimonials` - Get all testimonials
- `POST /testimonials` - Create testimonial (admin only)

### Contact
- `POST /contact` - Submit contact form

### Image Upload
- `POST /upload-image` - Upload image to Cloudinary (admin only)

## Frontend Integration

The backend is configured to work with a Next.js frontend running on `http://localhost:3000`. CORS is already enabled for this origin.

### Authentication Flow

1. Frontend sends login credentials to `/auth/login`
2. Backend returns JWT token
3. Frontend includes token in `Authorization: Bearer <token>` header for admin requests

### Image Upload Flow

1. Frontend sends image file to `/upload-image`
2. Backend uploads to Cloudinary
3. Backend returns image URL
4. Frontend uses URL for portfolio items

## Database Schema

### Users (Admin)
- `id` - Primary key
- `email` - Unique email address
- `password_hash` - Bcrypt hashed password
- `role` - User role (admin/user)
- `created_at` - Timestamp

### Portfolio Images
- `id` - Primary key
- `title` - Image title
- `category` - Image category
- `image_url` - Cloudinary URL
- `created_at` - Timestamp

### Bookings
- `id` - Primary key
- `name` - Client name
- `phone` - Client phone
- `email` - Client email
- `event_type` - Type of event
- `event_date` - Event date
- `message` - Additional message
- `status` - Booking status
- `created_at` - Timestamp

### Pricing
- `id` - Primary key
- `package_name` - Package name
- `price` - Package price
- `description` - Package description
- `created_at` - Timestamp

### Testimonials
- `id` - Primary key
- `client_name` - Client name
- `text` - Testimonial text
- `rating` - Rating (1-5)
- `created_at` - Timestamp

### Contacts
- `id` - Primary key
- `name` - Contact name
- `email` - Contact email
- `message` - Contact message
- `created_at` - Timestamp

## Database Migrations

### Create new migration
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback migration
```bash
alembic downgrade -1
```

## Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt for secure password storage
- **CORS Protection**: Configured for frontend domain
- **Input Validation**: Pydantic schemas for data validation
- **SQL Injection Prevention**: SQLAlchemy ORM protection

## Performance Features

- **Async Routes**: FastAPI async support
- **Database Indexing**: Optimized queries with indexes
- **Pagination**: Portfolio images with pagination
- **Connection Pooling**: SQLAlchemy connection management

## Deployment

### Environment Variables for Production
- Set `DEBUG=false`
- Use strong `SECRET_KEY`
- Configure production database URL
- Set up Cloudinary production credentials

### Production Server
```bash
# Using Gunicorn
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Monitoring

### Health Check
- `GET /health` - Application health status

### Logs
- Application logs available via stdout
- Database query logging configurable in settings

## Support

For issues and questions, please refer to the API documentation at `/docs` or contact the development team.
