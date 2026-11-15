# === Stage 7: Сортировка записей ===
# Project: CakeDesigner
import datetime


class CakeSorter:
    def __init__(self, cakes):
        self.cakes = list(cakes)

    def _sort_key(self, reverse):
        if reverse:
            return lambda cake: (-cake["created_at"], cake["name"])
        return lambda cake: (cake["created_at"], cake["name"])

    def by_name(self):
        return sorted(self.cakes, key=self._sort_key(False))

    def by_name_reverse(self):
        return sorted(self.cakes, key=self._sort_key(True))

    def by_date(self):
        return sorted(self.cakes, key=self._sort_key(False))

    def by_date_reverse(self):
        return sorted(self.cakes, key=self._sort_key(True))


def add_created_at(cakes):
    now = datetime.datetime.now()
    for cake in cakes:
        if "created_at" not in cake:
            cake["created_at"] = now
    return cakes


def sort_cakes(cakes, field, reverse):
    add_created_at(cakes)
    return sorted(cakes, key=lambda c: (c.get("created_at", datetime.datetime.min), c.get("name", "")),
                 reverse=reverse)
