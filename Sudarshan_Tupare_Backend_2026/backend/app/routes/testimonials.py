from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.testimonial import Testimonial
from app.schemas.testimonial import TestimonialCreate, TestimonialResponse
from app.auth.dependencies import get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[TestimonialResponse])
async def get_testimonials(db: Session = Depends(get_db)):
    testimonials = db.query(Testimonial).order_by(Testimonial.created_at.desc()).all()
    return testimonials

@router.post("/", response_model=TestimonialResponse)
async def create_testimonial(
    testimonial: TestimonialCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_testimonial = Testimonial(**testimonial.dict())
    db.add(db_testimonial)
    db.commit()
    db.refresh(db_testimonial)
    return db_testimonial
