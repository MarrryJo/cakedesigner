# === Stage 2: Проверка полей ===
# Project: CakeDesigner
import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Cake:
    name: str
    diameter: float
    filling: str
    price: float


def normalize_input(value: str) -> str:
    cleaned = value.strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"[^a-zа-яё0-9\s]", "", cleaned.lower())
    return cleaned


def validate_diameter(value: str) -> Optional[float]:
    cleaned = normalize_input(value)
    if not cleaned:
        return None
    try:
        diameter = float(cleaned)
    except ValueError:
        return None
    if diameter <= 0:
        return None
    return diameter


def validate_price(value: str) -> Optional[float]:
    cleaned = normalize_input(value)
    if not cleaned:
        return None
    try:
        price = float(cleaned)
    except ValueError:
        return None
    if price < 0:
        return None
    return price


def validate_name(value: str) -> str:
    cleaned = normalize_input(value)
    if not cleaned:
        raise ValueError("Название не может быть пустым.")
    if len(cleaned) > 50:
        raise ValueError("Название слишком длинное (не более 50 символов).")
    return cleaned


def validate_filling(value: str) -> str:
    cleaned = normalize_input(value)
    if not cleaned:
        raise ValueError("Начинка не может быть пустой.")
    if len(cleaned) > 50:
        raise ValueError("Начинка слишком длинная (не более 50 символов).")
    return cleaned


def build_cake(
    name: str,
    diameter: str,
    filling: str,
    price: str,
) -> Cake:
    cake_name = validate_name(name)
    cake_diameter = validate_diameter(diameter)
    cake_filling = validate_filling(filling)
    cake_price = validate_price(price)

    if cake_diameter is None:
        raise ValueError("Неверный диаметр: введите положительное число.")
    if cake_price is None:
        raise ValueError("Неверная цена: введите неотрицательное число.")

    return Cake(
        name=cake_name,
        diameter=cake_diameter,
        filling=cake_filling,
        price=cake_price,
    )
