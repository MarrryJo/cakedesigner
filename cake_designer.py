# === Stage 1: Каркас модуля ===
# Project: CakeDesigner
from dataclasses import dataclass


@dataclass
class Cake:
    name: str
    diameter: float
    filling: str
    price: float


def make_demo_cakes() -> list:
    return [
        Cake("Классический бисквит", 20.0, "сметанно-сливочный", 2400.0),
        Cake("Шоколадный рай", 24.0, "шоколадный", 3100.0),
        Cake("Фруктовый микс", 18.0, "фруктовый", 2700.0),
    ]


def main() -> None:
    cakes = make_demo_cakes()
    for cake in cakes:
        print(cake.name, "диаметр:", cake.diameter, "начинка:", cake.filling,
              "цена:", cake.price)
