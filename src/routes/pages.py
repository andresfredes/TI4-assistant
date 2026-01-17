from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/templates")
router = APIRouter()


@router.get("/admin", response_class=HTMLResponse)
async def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@router.get("/dev")
async def dev(request: Request):
    return templates.TemplateResponse("test.html", {"resquest": request})


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/player", response_class=HTMLResponse)
async def player(request: Request):
    return templates.TemplateResponse("player.html", {"request": request})
