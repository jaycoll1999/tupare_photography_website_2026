from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingResponse, BookingUpdate
from app.auth.dependencies import get_current_admin_user

router = APIRouter()

@router.post("/", response_model=BookingResponse)
async def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/", response_model=List[BookingResponse])
async def get_bookings(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    bookings = db.query(Booking).order_by(Booking.created_at.desc()).all()
    return bookings

@router.put("/{booking_id}", response_model=BookingResponse)
async def update_booking(
    booking_id: int,
    booking_update: BookingUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    db_booking.status = booking_update.status
    db.commit()
    db.refresh(db_booking)
    return db_booking
