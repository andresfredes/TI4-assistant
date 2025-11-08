from pydantic import BaseModel


class Faction(BaseModel):
    name: str
    icon_url: str


FACTIONS = [
    Faction(name="Last Bastion", icon_url="LastBastion.webp"),
    Faction(name="Sardakk N'orr", icon_url="Sardakk.png"),
    Faction(name="The Arborec", icon_url="Arborec.png"),
    Faction(name="The Argent Flight", icon_url="Argent.png"),
    Faction(name="The Barony of Letnev", icon_url="Barony.png"),
    Faction(name="The Crimson Rebellion", icon_url="Crimson.webp"),
    Faction(name="The Clan of Saar", icon_url="Saar.png"),
    Faction(name="The Council Keleres", icon_url="Keleres.webp"),
    Faction(name="The Deepwrought Scholarate", icon_url="Deepwrought.webp"),
    Faction(name="The Embers of Muaat", icon_url="Muaat.png"),
    Faction(name="The Emirates of Hacan", icon_url="Hacan.png"),
    Faction(name="The Empyrean", icon_url="Empyrean.png"),
    Faction(name="The Federation of Sol", icon_url="Sol.png"),
    Faction(name="The Firmament / The Obsidian", icon_url="Firmament.webp"),
    Faction(name="The Ghosts of Creuss", icon_url="Ghosts.png"),
    Faction(name="The L1Z1X Mindnet", icon_url="L1Z1X.png"),
    Faction(name="The Mahact Gene-Sorcerers", icon_url="Mahact.png"),
    Faction(name="The Mentak Coalition", icon_url="Mentak.png"),
    Faction(name="The Naalu Collective", icon_url="Naalu.png"),
    Faction(name="The Naaz-Rokha Alliance", icon_url="NaazRokha.png"),
    Faction(name="The Nekro Virus", icon_url="Nekro.png"),
    Faction(name="The Nomad", icon_url="Nomad.png"),
    Faction(name="The Ral Nel Consortium", icon_url="RalNel.webp"),
    Faction(name="The Titans of Ul", icon_url="Ul.png"),
    Faction(name="The Universities of Jol-Nar", icon_url="JolNar.png"),
    Faction(name="The Vuil'Raith Cabal", icon_url="Cabal.png"),
    Faction(name="The Winnu", icon_url="Winnu.png"),
    Faction(name="The Xxcha Kingdom", icon_url="Xxcha.png"),
    Faction(name="The Yin Brotherhood", icon_url="Yin.png"),
    Faction(name="The Yssaril Tribes", icon_url="Yssaril.png"),
]