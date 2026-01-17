from sqlmodel import Field, SQLModel

from src.models.enum import Colour
from src.models.faction import Faction


class PlayerBase(SQLModel):
    name: str = Field(index=True)
    position: int = Field(index=True)
    faction: Faction = Field()  # TODO relationship / foreign key
    colour: Colour = Field(index=True)
    score: int = Field(default=0, index=True)


class Player(PlayerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class PlayerCreate(PlayerBase):
    pass
