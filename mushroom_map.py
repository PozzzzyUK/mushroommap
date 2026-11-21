# === Stage 1: Каркас модуля ===
# Project: MushroomMap
from dataclasses import dataclass
from datetime import date


@dataclass
class Place:
    name: str
    forest: str
    season: str
    visit_date: date


def make_demo_places() -> list[Place]:
    return [
        Place("Утро в сосновом бору", "Сосновый бор", "осень", date(2024, 9, 14)),
        Place("Тёмный уголок у реки", "Смешанный лес", "осень", date(2024, 9, 15)),
        Place("Грибной холм", "Дубрава", "лето", date(2024, 8, 3)),
    ]


def main() -> None:
    places = make_demo_places()
    print("Карта грибных мест MushroomMap")
    print("-" * 30)
    for i, place in enumerate(places, start=1):
        print(f"{i}. {place.name}")
        print(f"   Лес: {place.forest}")
        print(f"   Сезон: {place.season}")
        print(f"   Дата: {place.visit_date}")
        print()


if __name__ == "__main__":
    main()
