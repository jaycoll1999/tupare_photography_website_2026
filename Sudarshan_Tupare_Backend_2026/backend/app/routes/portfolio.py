from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.database import get_db
from app.models.portfolio import PortfolioImage
from app.schemas.portfolio import PortfolioCreate, PortfolioResponse
from app.auth.dependencies import get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[PortfolioResponse])
async def get_portfolio(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(PortfolioImage)
    
    if category:
        query = query.filter(PortfolioImage.category == category)
    
    portfolio_images = query.order_by(desc(PortfolioImage.created_at)).offset(skip).limit(limit).all()
    return portfolio_images

@router.post("/", response_model=PortfolioResponse)
async def create_portfolio(
    portfolio: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_portfolio = PortfolioImage(**portfolio.dict())
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

@router.put("/{portfolio_id}", response_model=PortfolioResponse)
async def update_portfolio(
    portfolio_id: int,
    portfolio: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_portfolio = db.query(PortfolioImage).filter(PortfolioImage.id == portfolio_id).first()
    if not db_portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio image not found"
        )
    
    for key, value in portfolio.dict().items():
        setattr(db_portfolio, key, value)
    
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

@router.delete("/{portfolio_id}")
async def delete_portfolio(
    portfolio_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    db_portfolio = db.query(PortfolioImage).filter(PortfolioImage.id == portfolio_id).first()
    if not db_portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio image not found"
        )
    
    db.delete(db_portfolio)
    db.commit()
    return {"message": "Portfolio image deleted successfully"}
