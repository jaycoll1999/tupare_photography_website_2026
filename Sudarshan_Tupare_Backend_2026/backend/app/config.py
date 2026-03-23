from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Cloudinary
    CLOUDINARY_NAME: str
    CLOUDINARY_KEY: str
    CLOUDINARY_SECRET: str
    
    # Environment
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()
