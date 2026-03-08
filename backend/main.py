from fastapi import FastAPI
from backend.api.routes_detect import router as detect_router
from backend.api.routes_crops import router as crop_router

app = FastAPI(title="AgroAI API")

app.include_router(detect_router)
app.include_router(crop_router)

@app.get("/")
def root():
    return {"status": "AgroAI running"}
