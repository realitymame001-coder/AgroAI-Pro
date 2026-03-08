from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/crops")
def crops():
    with open("knowledge-base/crops/vegetables.json") as f:
        return json.load(f)
