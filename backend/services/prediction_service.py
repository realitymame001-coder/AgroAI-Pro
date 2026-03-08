from fastapi import UploadFile
import shutil
import os

async def detect_disease(file: UploadFile):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    # placeholder prediction
    disease = "early_blight"

    return {
        "disease": disease,
        "treatment": "Neem oil spray or Mancozeb fungicide"
    }
