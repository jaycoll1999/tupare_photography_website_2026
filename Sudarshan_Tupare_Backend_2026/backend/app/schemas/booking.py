from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from app.models.booking import BookingStatus

class BookingCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    event_type: str
    event_date: date
    message: str = None

class BookingUpdate(BaseModel):
    status: BookingStatus

class BookingResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    event_type: str
    event_date: date
    message: str
    status: BookingStatus
    created_at: datetime
    
    class Config:
        from_attributes = True
