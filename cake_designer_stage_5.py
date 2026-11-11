# === Stage 5: Удаление и восстановление ===
# Project: CakeDesigner
class SoftDeletedCake:
    def __init__(self, cake_id, name, diameter, filling, price, is_deleted=False):
        self.cake_id = cake_id
        self.name = name
        self.diameter = diameter
        self.filling = filling
        self.price = price
        self.is_deleted = is_deleted


class CakeStore:
    def __init__(self):
        self.cakes = []
        self._next_id = 1

    def create_cake(self, name, diameter, filling, price):
        cake = SoftDeletedCake(
            self._next_id, name, diameter, filling, price
        )
        self.cakes.append(cake)
        self._next_id += 1
        return cake

    def get_active_cake(self, cake_id):
        for cake in self.cakes:
            if cake.cake_id == cake_id and not cake.is_deleted:
                return cake
        return None

    def get_deleted_cake(self, cake_id):
        for cake in self.cakes:
            if cake.cake_id == cake_id and cake.is_deleted:
                return cake
        return None

    def delete_cake(self, cake_id):
        cake = self.get_active_cake(cake_id)
        if cake is not None:
            cake.is_deleted = True
            return True
        return False

    def restore_cake(self, cake_id):
        cake = self.get_deleted_cake(cake_id)
        if cake is not None:
            cake.is_deleted = False
            return True
        return False

    def list_active_cakes(self):
        return [cake for cake in self.cakes if not cake.is_deleted]

    def list_deleted_cakes(self):
        return [cake for cake in self.cakes if cake.is_deleted]


def main():
    store = CakeStore()
    cake = store.create_cake("Ванильный", 20, "Сметанный крем", 1500)
    print("Создан торт:", cake.name, "ID:", cake.cake_id)
    print("Активных тортов:", len(store.list_active_cakes()))

    store.delete_cake(cake.cake_id)
    print("После удаления активных тортов:", len(store.list_active_cakes()))
    print("Удалённых тортов:", len(store.list_deleted_cakes()))

    store.restore_cake(cake.cake_id)
    print("После восстановления активных тортов:", len(store.list_active_cakes()))
    print("Восстановлен торт:", store.get_active_cake(cake.cake_id).name)


if __name__ == "__main__":
    main()
