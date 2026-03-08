from fastapi import APIRouter, UploadFile
from backend.services.prediction_service import detect_disease

router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile):
    return await detect_disease(file)
