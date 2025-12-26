from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from src.core.templates import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
