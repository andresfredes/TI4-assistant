from fastapi import FastAPI
from src.routes.dev import router as dev_router
from src.routes.admin import router as admin_router
from src.routes.player import router as player_router

app = FastAPI()

app.include_router(dev_router)
app.include_router(admin_router)
app.include_router(player_router)

