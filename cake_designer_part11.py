# === Stage 11: Массовое обновление ===
# Project: CakeDesigner
from __future__ import annotations


class Cake:
    def __init__(self, name, diameter, filling, price):
        self.name = name
        self.diameter = diameter
        self.filling = filling
        self.price = price

    def __repr__(self):
        return f"Cake({self.name}, {self.diameter}, {self.filling}, {self.price})"


class Layer:
    def __init__(self, name, radius, height, cake_price, decoration_price):
        self.name = name
        self.radius = radius
        self.height = height
        self.cake_price = cake_price
        self.decoration_price = decoration_price

    def volume(self):
        return 3.141592653589793 * self.radius ** 2 * self.height

    def cost(self):
        return self.cake_price * self.volume() + self.decoration_price * self.height

    def __repr__(self):
        return f"Layer({self.name}, r={self.radius}, h={self.height})"


class CakeDesigner:
    def __init__(self):
        self.cakes = []
        self.layers = []
        self._build_layers()

    def add_cake(self, cake):
        self.cakes.append(cake)

    def add_layer(self, layer):
        self.layers.append(layer)

    def _build_layers(self):
        self.add_layer(Layer("base", 10.0, 8.0, 120.0, 30.0))
        self.add_layer(Layer("middle", 8.0, 6.0, 100.0, 25.0))
        self.add_layer(Layer("top", 6.0, 4.0, 80.0, 20.0))

    def estimate(self, cake):
        total = 0.0
        for layer in self.layers:
            if layer.radius <= cake.diameter:
                total += layer.cost()
        return total

    def preview_changes(self, predicate, new_value):
        changed = []
        for cake in self.cakes:
            if predicate(cake):
                old = cake.price
                new_price = old * 1.1 if new_value == "up" else old * 0.9
                changed.append((cake, old, new_price))
        return changed

    def apply_changes(self, predicate, new_value):
        changed = self.preview_changes(predicate, new_value)
        for cake, old_price, new_price in changed:
            cake.price = new_price
        return changed

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for cake in self.cakes:
                file.write(
                    f"{cake.name}|{cake.diameter}|{cake.filling}|{cake.price}\n"
                )

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                name = parts[0]
                diameter = float(parts[1])
                filling = parts[2]
                price = float(parts[3])
                self.add_cake(Cake(name, diameter, filling, price))


if __name__ == "__main__":
    designer = CakeDesigner()
    designer.add_cake(Cake("Сендвич", 20.0, "сливки", 1500.0))
    designer.add_cake(Cake("Мусс", 15.0, "мороженое", 1200.0))
    designer.add_cake(Cake("Фруктовый", 25.0, "джем", 1800.0))

    target = lambda cake: cake.diameter > 20
    changes = designer.preview_changes(target, "up")
    print("Предварительный просмотр изменений:")
    for cake, old_price, new_price in changes:
        print(f"  {cake.name}: {old_price} -> {new_price:.2f}")

    if changes:
        designer.apply_changes(target, "up")
        print("Изменения применены.")

    print("Итоговая смета:")
    for cake in designer.cakes:
        print(f"  {cake.name}: {cake.price:.2f}")

    designer.save("cakes.txt")
    print("Данные сохранены в cakes.txt")
