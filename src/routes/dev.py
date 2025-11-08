from fastapi import APIRouter

router = APIRouter(prefix="/dev", tags=["dev"])

@router.get("/")
def home():
    return {"message": "Dev Home"}