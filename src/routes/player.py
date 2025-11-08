from fastapi import APIRouter

router = APIRouter(tags=["player"])

@router.get("/")
def home():
    return {"message": "Player Home"}