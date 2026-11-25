# === Stage 3: Хранилище в памяти ===
# Project: MushroomMap
import uuid
from datetime import date


class Place:
    """Грибное место: название, лес, сезон, дата и уникальный идентификатор."""

    def __init__(self, name, forest, season, day, month, year):
        self.id = uuid.uuid4()
        self.name = name
        self.forest = forest
        self.season = season
        self.day = day
        self.month = month
        self.year = year
        self._next_id = str(self.id)

    def __repr__(self):
        return f"Place(id={self.id}, name={self.name!r}, forest={self.forest!r}, season={self.season!r}, date={date(self.year, self.month, self.day)})"


PLACE_STORE = {}


def add_place(name, forest, season, day, month, year):
    place = Place(name, forest, season, day, month, year)
    PLACE_STORE[place.id] = place
    return place


def get_place(place_id):
    return PLACE_STORE.get(place_id)


def list_places():
    return list(PLACE_STORE.values())
