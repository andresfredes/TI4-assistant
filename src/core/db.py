from sqlmodel import SQLModel, create_engine

from src.core.config import get_settings

connect_args = {"check_same_thread": False}
engine = create_engine(get_settings().db_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
