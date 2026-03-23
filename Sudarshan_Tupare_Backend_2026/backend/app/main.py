from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine
from app.models import Base
from app.routes import auth, portfolio, bookings, pricing, testimonials, contact, upload

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sudarshan Tupare Photography API",
    description="Backend API for professional photography website",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])
app.include_router(bookings.router, prefix="/booking", tags=["Bookings"])
app.include_router(pricing.router, prefix="/pricing", tags=["Pricing"])
app.include_router(testimonials.router, prefix="/testimonials", tags=["Testimonials"])
app.include_router(contact.router, prefix="/contact", tags=["Contact"])
app.include_router(upload.router, prefix="/upload-image", tags=["Image Upload"])

@app.get("/")
async def root():
    return {"message": "Sudarshan Tupare Photography API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
