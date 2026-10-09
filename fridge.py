# Проект "Холодильник"

from decimal import Decimal
from datetime import date, datetime
import pandas as pd

D_FORMAT = "%Y-%m-%d"

items = {
    "Пельмени Универсальные": [
        {"amount": Decimal("0.5"), "expiration_date": date(2023, 7, 15)},
        {"amount": Decimal("2"), "expiration_date": date(2023, 8, 1)},
    ],
    "Вода": [{"amount": Decimal("1.5"), "expiration_date": None}],
}


def fridge(items):
    """
    Показывает содержимое "холодильника" в удобном формате
    """
    s = pd.Series(items).explode()
    df = pd.DataFrame(s.tolist(), index=s.index).reset_index(names="Продукт")
    print(df)


def add(items, title, amount, expiration_date=None):
    """
    Добавляет продукты в словарь items.

    Parameters:
        - items (dict): словарь с продуктами
        - title (str): название продукта
        - amount (Decimal): количество продукта
        - expiration_date (date): срок годности в формате "YYYY-MM-DD" или None
    """

    if expiration_date != None:
        if title in items:
            items[title].append(
                {
                    "amount": amount,
                    "expiration_date": datetime.strptime(
                        expiration_date, D_FORMAT
                    ).date(),
                }
            )
        else:
            items[title] = [
                {
                    "amount": amount,
                    "expiration_date": datetime.strptime(
                        expiration_date, D_FORMAT
                    ).date(),
                }
            ]
    else:
        if title in items:
            items[title].append({"amount": amount, "expiration_date": expiration_date})
        else:
            items[title] = [{"amount": amount, "expiration_date": expiration_date}]

    print("\nПродукт был добавлен!\n")


def add_by_note(items, note):
    """
    Добавляет продукты из текстовой записи формата
        "Название продукта Количество Дата" или "Название продукта Количество".

    Parameters:
        - items (dict): словарь с продуктами
        - note: строка с описанием продукта
    """

    pieces = note.split()
    if "-" in pieces[-1] and pieces[-1].count("-") == 2:
        expiration_date = pieces[-1]
        amount = Decimal(pieces[-2])
        title = " ".join(pieces[:-2])

    else:
        expiration_date = None
        amount = pieces[-1]
        title = " ".join(pieces[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    """
    Ищет продукты, название которых содержит
        поисковый запрос needle (без учёта регистра).

    Parameters:
        - items (dict): словарь с продуктами
        - needle (str): поисковый запрос

    Returns:
        - список названий найденных продуктов
    """

    res = []
    for key in items:
        if needle.lower() in key.lower():
            res.append(key)

    return res


def amount(items, needle):
    """
    Подсчитывает общее кол-во продуктов,
        подходящих под поисковый запрос.

    Parameters:
        - items (dict): словарь с продуктами
        - needle (str): поисковый запрос

    Returns:
        - res (Decimal): общее количество
    """

    res = 0
    exist = find(items, needle)
    if exist:
        for product in exist:
            needle = product
            for k in items[needle]:
                res += k["amount"]
    return Decimal(res)
