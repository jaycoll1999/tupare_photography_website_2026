from pydantic import BaseModel, Field
from datetime import datetime

class TestimonialCreate(BaseModel):
    client_name: str
    text: str
    rating: int = Field(..., ge=1, le=5, description="Rating must be between 1 and 5")

class TestimonialResponse(BaseModel):
    id: int
    client_name: str
    text: str
    rating: int
    created_at: datetime
    
    class Config:
        from_attributes = True
