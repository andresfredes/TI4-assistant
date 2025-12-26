from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routes.admin import router as admin_router
from src.routes.home import router as home_router
from src.routes.player import router as player_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(home_router)
app.include_router(admin_router)
app.include_router(player_router)
