from pydantic import BaseModel

from src.models.player import Player


class Game(BaseModel):
    round: int
    players: list[Player]