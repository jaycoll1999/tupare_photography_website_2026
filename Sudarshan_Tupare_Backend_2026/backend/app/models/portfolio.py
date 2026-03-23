from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from app.database import Base

class PortfolioImage(Base):
    __tablename__ = "portfolio_images"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False, index=True)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Add index for performance
    __table_args__ = (
        Index('idx_category_created', 'category', 'created_at'),
    )
