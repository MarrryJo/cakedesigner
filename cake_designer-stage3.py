# === Stage 3: Хранилище в памяти ===
# Project: CakeDesigner
memory_store.py

from uuid import uuid4


class Cake:
    def __init__(self, name, diameter, filling, price):
        self.id = uuid4().hex
        self.name = name
        self.diameter = diameter
        self.filling = filling
        self.price = price

    def __repr__(self):
        return f"Cake(id={self.id}, name={self.name}, diameter={self.diameter}, filling={self.filling}, price={self.price})"


class CakeStore:
    def __init__(self):
        self._cakes = {}

    def add_cake(self, cake):
        if not isinstance(cake, Cake):
            raise TypeError("Только объекты класса Cake можно хранить в хранилище")
        if cake.id in self._cakes:
            raise KeyError(f"Торт с идентификатором {cake.id} уже существует")
        self._cakes[cake.id] = cake
        return cake

    def get_cake(self, cake_id):
        if cake_id not in self._cakes:
            raise KeyError(f"Торт с идентификатором {cake_id} не найден")
        return self._cakes[cake_id]

    def list_cakes(self):
        return list(self._cakes.values())


if __name__ == "__main__":
    store = CakeStore()

    cake1 = Cake("Клубничный", 20, "Сметанный крем", 1500)
    cake2 = Cake("Шоколадный", 25, "Бисквитный", 2200)
    store.add_cake(cake1)
    store.add_cake(cake2)

    print("Добавлено тортов:", len(store.list_cakes()))
    print(store.get_cake(cake1.id))

    try:
        store.get_cake("does-not-exist")
    except KeyError as err:
        print("Ошибка:", err)

    try:
        store.add_cake(cake1)
    except KeyError as err:
        print("Ошибка:", err)
