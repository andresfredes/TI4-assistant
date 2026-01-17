from sqlmodel import Field, SQLModel

from src.models.enum import Expansion


class FactionBase(SQLModel):
    name: str = Field(index=True)
    icon_url: str = Field(index=True)
    expansion: Expansion = Field(index=True)


class Faction(FactionBase, table=True):
    id: int = Field(index=True, primary_key=True)


class FactionCreate(FactionBase):
    pass


FACTIONS = [
    FactionCreate(expansion=Expansion.TE, name="Last Bastion", icon_url="LastBastion.webp"),
    FactionCreate(expansion=Expansion.BASE, name="Sardakk N'orr", icon_url="Sardakk.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Arborec", icon_url="Arborec.png"),
    FactionCreate(expansion=Expansion.POK, name="The Argent Flight", icon_url="Argent.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Barony of Letnev", icon_url="Barony.png"),
    FactionCreate(expansion=Expansion.TE, name="The Crimson Rebellion", icon_url="Crimson.webp"),
    FactionCreate(expansion=Expansion.BASE, name="The Clan of Saar", icon_url="Saar.png"),
    FactionCreate(expansion=Expansion.TE, name="The Council Keleres", icon_url="Keleres.webp"),
    FactionCreate(expansion=Expansion.TE, name="The Deepwrought Scholarate", icon_url="Deepwrought.webp"),
    FactionCreate(expansion=Expansion.BASE, name="The Embers of Muaat", icon_url="Muaat.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Emirates of Hacan", icon_url="Hacan.png"),
    FactionCreate(expansion=Expansion.POK, name="The Empyrean", icon_url="Empyrean.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Federation of Sol", icon_url="Sol.png"),
    FactionCreate(expansion=Expansion.TE, name="The Firmament / The Obsidian", icon_url="Firmament.webp"),
    FactionCreate(expansion=Expansion.BASE, name="The Ghosts of Creuss", icon_url="Ghosts.png"),
    FactionCreate(expansion=Expansion.BASE, name="The L1Z1X Mindnet", icon_url="L1Z1X.png"),
    FactionCreate(expansion=Expansion.POK, name="The Mahact Gene-Sorcerers", icon_url="Mahact.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Mentak Coalition", icon_url="Mentak.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Naalu Collective", icon_url="Naalu.png"),
    FactionCreate(expansion=Expansion.POK, name="The Naaz-Rokha Alliance", icon_url="NaazRokha.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Nekro Virus", icon_url="Nekro.png"),
    FactionCreate(expansion=Expansion.POK, name="The Nomad", icon_url="Nomad.png"),
    FactionCreate(expansion=Expansion.TE, name="The Ral Nel Consortium", icon_url="RalNel.webp"),
    FactionCreate(expansion=Expansion.POK, name="The Titans of Ul", icon_url="Ul.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Universities of Jol-Nar", icon_url="JolNar.png"),
    FactionCreate(expansion=Expansion.POK, name="The Vuil'Raith Cabal", icon_url="Cabal.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Winnu", icon_url="Winnu.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Xxcha Kingdom", icon_url="Xxcha.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Yin Brotherhood", icon_url="Yin.png"),
    FactionCreate(expansion=Expansion.BASE, name="The Yssaril Tribes", icon_url="Yssaril.png"),
]
