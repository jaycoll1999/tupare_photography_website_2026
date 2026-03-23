#!/usr/bin/env python3
"""
Script to create initial admin user for the photography backend.
Run this script after setting up the database to create your first admin account.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import User, UserRole, Base
from app.utils.security import hash_password
from app.config import settings

def create_admin_user():
    """Create the initial admin user"""
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if admin user already exists
        existing_admin = db.query(User).filter(User.email == "admin@sudarshanphotography.com").first()
        if existing_admin:
            print("Admin user already exists!")
            return
        
        # Get admin details from user
        print("Creating initial admin user...")
        email = input("Enter admin email (default: admin@sudarshanphotography.com): ").strip()
        if not email:
            email = "admin@sudarshanphotography.com"
        
        password = input("Enter admin password: ").strip()
        if not password:
            print("Password cannot be empty!")
            return
        
        # Create admin user
        hashed_password = hash_password(password)
        admin_user = User(
            email=email,
            password_hash=hashed_password,
            role=UserRole.ADMIN
        )
        
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        
        print(f"✅ Admin user created successfully!")
        print(f"   Email: {admin_user.email}")
        print(f"   Role: {admin_user.role.value}")
        print(f"\nYou can now login at http://localhost:8000/docs")
        print(f"Use the /auth/login endpoint with your credentials")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_admin_user()
