from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.contact import Contact
from app.schemas.contact import ContactCreate

router = APIRouter()

@router.post("/")
async def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    return {"message": "Contact form submitted successfully"}
