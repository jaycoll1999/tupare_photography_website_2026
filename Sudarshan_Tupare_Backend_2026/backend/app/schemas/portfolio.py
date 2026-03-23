from pydantic import BaseModel
from datetime import datetime

class PortfolioCreate(BaseModel):
    title: str
    category: str
    image_url: str

class PortfolioResponse(BaseModel):
    id: int
    title: str
    category: str
    image_url: str
    created_at: datetime
    
    class Config:
        from_attributes = True
