from pydantic import BaseModel
from datetime import datetime

class PricingCreate(BaseModel):
    package_name: str
    price: float
    description: str = None

class PricingResponse(BaseModel):
    id: int
    package_name: str
    price: float
    description: str
    created_at: datetime
    
    class Config:
        from_attributes = True
