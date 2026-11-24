# === Stage 2: Проверка полей ===
# Project: MushroomMap
def normalize_input(value):
    return (value or "").strip()


def parse_date(value):
    normalized = normalize_input(value)
    if not normalized:
        return None
    try:
        return datetime.datetime.strptime(normalized, "%Y-%m-%d").date()
    except ValueError:
        return None


DATE_FORMAT = "%Y-%m-%d"


def normalize_date(value):
    return parse_date(value)


def normalize_season(value):
    normalized = normalize_input(value).lower()
    valid_seasons = {"spring", "summer", "autumn", "winter"}
    if normalized and normalized in valid_seasons:
        return normalized
    if not value:
        return None
    return None


SEASONS = ("spring", "summer", "autumn", "winter")


def normalize_forest(value):
    normalized = normalize_input(value)
    if not normalized:
        return None
    return normalized


def normalize_name(value):
    normalized = normalize_input(value)
    if not normalized:
        return None
    if len(normalized) < 2:
        return None
    return normalized


def validate_place(place):
    errors = []
    if not place.name:
        errors.append("Название места не может быть пустым.")
    if not place.forest:
        errors.append("Укажите, в каком лесу находится место.")
    if not place.season:
        errors.append("Укажите сезон.")
    else:
        if place.season not in SEASONS:
            errors.append(
                "Неверный сезон. Доступные значения: "
                + ", ".join(SEASONS)
                + "."
            )
    if not place.date:
        errors.append("Укажите дату.")
    else:
        if not isinstance(place.date, datetime.date):
            errors.append("Дата должна быть в формате ДД.ММ.ГГГГ.")
    return errors
