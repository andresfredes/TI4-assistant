from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.models.faction import FACTIONS

router = APIRouter(prefix="/api")
templates = Jinja2Templates(directory="src/templates")

# TODO: add settings
FRAGMENTS_PATH = "template/fragments"


@router.get("/list-factions")
def list_factions(request: Request):
    return templates.TemplateResponse("fragments/factions.html", {"request": request, "factions": FACTIONS})


# def list_fragments():
#     return [p for p in os.listdir(FRAGMENTS_PATH) if p.endswith(".html")]


# @router.get("/render-fragment/{name}")
# async def render_fragment(request: Request, name: str):
#     fragments = list_fragments()
#     if name not in fragments:
#         return HTMLResponse("<div>Fragment not found</div>", status_code=404)
#     return HTMLResponse()
