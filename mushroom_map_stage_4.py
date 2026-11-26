# === Stage 4: Редактирование записей ===
# Project: MushroomMap
import datetime

ALLOWED_FIELDS = ("название", "лес", "сезон", "дата")
VALID_SEASONS = ("весна", "лето", "осень", "зима")


class Place:
    def __init__(self, place_id, name, forest, season, date):
        self.place_id = place_id
        self.name = name
        self.forest = forest
        self.season = season
        self.date = date


def _validate_value(field):
    if field == "сезон":
        if not isinstance(field, str) or field not in VALID_SEASONS:
            return False
        return True
    if field == "дата":
        if not isinstance(field, str):
            return False
        try:
            datetime.datetime.strptime(field, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    if field == "название":
        if not isinstance(field, str) or not field.strip():
            return False
        return True
    if field == "лес":
        if not isinstance(field, str) or not field.strip():
            return False
        return True
    return False


def edit_place(place, changes):
    new_place = Place(
        place.place_id,
        place.name,
        place.forest,
        place.season,
        place.date,
    )
    for field, value in changes.items():
        if field not in ALLOWED_FIELDS:
            raise ValueError(f"Поле '{field}' не допустимо для редактирования")
        if field == "place_id":
            raise ValueError("ID места изменять нельзя")
        if not _validate_value(field):
            raise ValueError(f"Значение для поля '{field}' недопустимо")
        setattr(new_place, field, value)
    return new_place
