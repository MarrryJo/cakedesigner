# === Stage 4: Редактирование записей ===
# Project: CakeDesigner
from copy import deepcopy


ALLOWED_FIELDS = {"название", "диаметр", "начинка", "цена"}


def validate_cake_fields(cake, changed_fields):
    if not isinstance(cake, dict):
        raise ValueError("Торт должен быть словарём")
    for field in changed_fields:
        if field not in ALLOWED_FIELDS:
            raise ValueError(f"Недопустимое поле для редактирования: {field}")
        if field not in cake:
            raise ValueError(f"Отсутствует поле в торта: {field}")
    if "диаметр" in changed_fields:
        diameter = cake["диаметр"]
        if not isinstance(diameter, (int, float)) or diameter <= 0:
            raise ValueError("Диаметр должен быть положительным числом")
    if "цена" in changed_fields:
        price = cake["цена"]
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть неотрицательным числом")
    if "начинка" in changed_fields and cake["начинка"] is None:
        raise ValueError("Начинка не может быть пустой")
    if "название" in changed_fields and cake["название"] is None:
        raise ValueError("Название не может быть пустым")


def edit_cake(cake, changes):
    if not isinstance(changes, dict):
        raise TypeError("Изменения должны быть словарём")
    changed_fields = set(changes.keys())
    validate_cake_fields(cake, changed_fields)
    updated = deepcopy(cake)
    for field, value in changes.items():
        updated[field] = value
    return updated


def recalculate_price(cake):
    radius = cake["диаметр"] / 2
    area = 3.14159 * radius * radius
    base = area * cake["цена"]
    return round(base, 2)


def estimate_cake(cake, layers):
    total_layers = len(layers)
    total_diameter = max([cake["диаметр"]] + [layer["диаметр"] for layer in layers])
    total_price = recalculate_price(cake)
    for layer in layers:
        layer_price = recalculate_price(layer)
        total_price += layer_price
    return {"название": cake["название"], "диаметр": total_diameter, "начинка": cake["начинка"], "цена": total_price}
