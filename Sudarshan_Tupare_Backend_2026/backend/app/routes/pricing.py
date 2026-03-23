from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pricing import Pricing
from app.schemas.pricing import PricingCreate, PricingResponse
from app.auth.dependencies import get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[PricingResponse])
async def get_pricing(db: Session = Depends(get_db)):
    pricing_plans = db.query(Pricing).order_by(Pricing.created_at.asc()).all()
    return pricing_plans

@router.post("/", response_model=PricingResponse)
async def create_pricing(
    pricing: PricingCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_pricing = Pricing(**pricing.dict())
    db.add(db_pricing)
    db.commit()
    db.refresh(db_pricing)
    return db_pricing

@router.put("/{pricing_id}", response_model=PricingResponse)
async def update_pricing(
    pricing_id: int,
    pricing: PricingCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_pricing = db.query(Pricing).filter(Pricing.id == pricing_id).first()
    if not db_pricing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pricing plan not found"
        )
    
    for key, value in pricing.dict().items():
        setattr(db_pricing, key, value)
    
    db.commit()
    db.refresh(db_pricing)
    return db_pricing
