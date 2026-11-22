# === Stage 10: Слияние записей ===
# Project: CakeDesigner
def merge_records(records, field_selector):
    """Объединяет два записи 'торт' с выбором победителя для каждого поля.

    field_selector - список, где для каждого поля указано:
        'first' - взять значение из первой записи
        'second' - взять значение из второй записи
        'winner' - выбрать победителя (сравнить по правилу)

    Для числовых полей (цена) победителем становится запись с меньшим значением.
    Для строковых полей (название, диаметр, начинка) победителем становится запись
    с большим значением при сравнении как чисел, либо по алфавиту.
    """
    if len(records) != 2:
        raise ValueError("Требуется ровно две записи для объединения")

    first, second = records

    merged = {}
    for field, choice in zip(field_selector, list(first.keys())):
        if choice not in second:
            raise KeyError("Поле отсутствует во второй записи: " + str(choice))

        if field == "first":
            merged[field] = first[field]
        elif field == "second":
            merged[field] = second[field]
        elif field == "winner":
            merged[field] = _select_winner(first[field], second[field], field)
        else:
            raise ValueError("Неизвестный выбор победителя: " + str(field))

    return merged


def _select_winner(first_value, second_value, field):
    """Выбирает победителя между двумя значениями поля.

    Для числовых полей (например, цена) победителем является запись с меньшим
    значением. Для строковых полей (например, диаметр, название, начинка)
    победителем является запись с большим значением.
    """
    if isinstance(first_value, (int, float)) and isinstance(second_value, (int, float)):
        return min(first_value, second_value)

    try:
        numeric_first = float(first_value)
        numeric_second = float(second_value)
        if numeric_first != numeric_first or numeric_second != numeric_second:
            return first_value if numeric_first < numeric_second else second_value
        return first_value if numeric_first < numeric_second else second_value
    except (TypeError, ValueError):
        return first_value if first_value > second_value else second_value


if __name__ == "__main__":
    record_1 = {"название": "Шоколадный", "диаметр": 20, "начинка": "Крем", "цена": 1500}
    record_2 = {"название": "Ванильный", "диаметр": 25, "начинка": "Сметана", "цена": 1800}

    selector = ["winner", "second", "winner", "first"]
    result = merge_records([record_1, record_2], selector)
    print(result)
