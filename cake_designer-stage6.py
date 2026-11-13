# === Stage 6: Связи между сущностями ===
# Project: CakeDesigner
from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class Layer:
    id: int
    cake_id: int
    name: str
    diameter: float
    height: float
    filling: Optional[str] = None

    def volume(self) -> float:
        radius = self.diameter / 2
        return 3.141592653589793 * radius * radius * self.height


@dataclass
class Cake:
    id: int
    name: str
    diameter: float
    filling: str
    price: float
    layers: List[Layer] = None

    def __post_init__(self):
        if self.layers is None:
            self.layers = []


def link_integrity(cake: Cake) -> Dict[str, Any]:
    problems: List[str] = []
    for layer in cake.layers:
        if layer.cake_id != cake.id:
            problems.append(
                f"Ярус {layer.id} ({layer.name}) привязан к торту {layer.cake_id}, "
                f"а не к торту {cake.id}"
            )
        if layer.diameter <= 0:
            problems.append(
                f"Ярус {layer.id} ({layer.name}) имеет недопустимый диаметр {layer.diameter}"
            )
        if layer.height <= 0:
            problems.append(
                f"Ярус {layer.id} ({layer.name}) имеет недопустимую высоту {layer.height}"
            )
    return {"problems": problems, "is_valid": len(problems) == 0}


def fetch_layers(cake: Cake) -> List[Layer]:
    return list(cake.layers)


def total_volume(cake: Cake) -> float:
    return sum(layer.volume() for layer in cake.layers)


def build_cake(layers: List[Layer], name: str, diameter: float,
               filling: str, price: float, cake_id: int) -> Cake:
    cake = Cake(id=cake_id, name=name, diameter=diameter,
                filling=filling, price=price)
    for layer in layers:
        layer.cake_id = cake_id
        cake.layers.append(layer)
    return cake


if __name__ == "__main__":
    layers = [
        Layer(id=1, cake_id=100, name="Нижний", diameter=22.0, height=8.0, filling="Сметанный"),
        Layer(id=2, cake_id=100, name="Верхний", diameter=16.0, height=6.0, filling=None),
    ]
    cake = build_cake(layers, "С Днем Рождения", 22.0, "Сметанный", 3500.0, cake_id=100)
    integrity = link_integrity(cake)
    print("Связь корректна:", integrity["is_valid"])
    print("Общий объем:", round(total_volume(cake), 2), "см³")
    for layer in fetch_layers(cake):
        print(f"Ярус {layer.id}: {layer.name}, объем {round(layer.volume(), 2)} см³")
