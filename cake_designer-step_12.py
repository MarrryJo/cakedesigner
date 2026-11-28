# === Stage 12: Избранное ===
# Project: CakeDesigner
from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Cake:
    name: str
    diameter: float
    filling: str
    price: float
    favorite: bool = False


class CakeFavorites:
    def __init__(self):
        self.selected: Set[int] = set()

    def is_favorite(self, cake_id: int) -> bool:
        return cake_id in self.selected

    def toggle(self, cake_id: int) -> None:
        if cake_id in self.selected:
            self.selected.discard(cake_id)
        else:
            self.selected.add(cake_id)

    def add(self, cake_id: int) -> None:
        self.selected.add(cake_id)

    def remove(self, cake_id: int) -> None:
        self.selected.discard(cake_id)

    def list_selected(self, cakes: List[Cake]) -> List[Cake]:
        return [cake for cake in cakes if self.is_favorite(cake.id)]

    def count(self) -> int:
        return len(self.selected)
