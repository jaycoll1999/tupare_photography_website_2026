from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader
from app.database import get_db
from app.config import settings
from app.auth.dependencies import get_current_admin_user

router = APIRouter()

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_NAME,
    api_key=settings.CLOUDINARY_KEY,
    api_secret=settings.CLOUDINARY_SECRET
)

@router.post("/")
async def upload_image(
    file: UploadFile = File(...),
    current_user = Depends(get_current_admin_user)
):
    # Validate file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be an image"
        )
    
    try:
        # Upload to Cloudinary
        result = cloudinary.uploader.upload(
            file.file,
            folder="sudarshan_photography",
            resource_type="image",
            quality="auto",
            fetch_format="auto"
        )
        
        return {
            "url": result["secure_url"],
            "public_id": result["public_id"]
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to upload image: {str(e)}"
        )
