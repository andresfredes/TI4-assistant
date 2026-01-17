from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.core.db import create_db_and_tables
from src.routes.api import router as api_router
from src.routes.pages import router as pages_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # app start up
    create_db_and_tables()
    yield
    # app clean up


app = FastAPI(lifespan=lifespan)


app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(pages_router)
app.include_router(api_router)
