from pydantic import BaseModel

from src.models.faction import Faction


class Player(BaseModel):
    id: int
    name: str
    faction: Faction
    colour: str
    score: int