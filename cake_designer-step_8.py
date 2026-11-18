# === Stage 8: Теги ===
# Project: CakeDesigner
from typing import List


class Tag:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Tag) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Tag({self.name!r})"


class Cake:
    def __init__(self, name: str, diameter: float, filling: str, price: float):
        self.name = name
        self.diameter = diameter
        self.filling = filling
        self.price = price
        self.tags: List[Tag] = []

    def add_tag(self, tag_name: str) -> None:
        tag = Tag(tag_name)
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag_name: str) -> bool:
        tag = Tag(tag_name)
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def has_tag(self, tag_name: str) -> bool:
        return Tag(tag_name) in self.tags

    def find_by_tag(self, tag_name: str):
        result = [cake for cake in self._iter_cakes() if cake.has_tag(tag_name)]
        return result

    @staticmethod
    def _iter_cakes():
        raise NotImplementedError("Реализовать в основном модуле проекта.")
