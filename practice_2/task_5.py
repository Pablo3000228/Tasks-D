ROMAN_TABLE = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(number: int) -> str:
    """
    Обычное число -> римское.

    Parameters:
        number: Число в привычном виде (обычное).

    Returns:
        str: Римское число.
    """
    result = ""
    for value, symbol in ROMAN_TABLE:
        while number >= value:
            result += symbol
            number -= value
    return result


def from_roman(roman: str) -> int:
    """
    Римское число -> обычное.

    Parameters:
        roman: Римское число.

    Returns:
        int: Число в привычном виде (обычное).
    """
    result = 0
    for i, char in enumerate(roman):
        value = ROMAN_VALUES[char]
        # Если справа стоит большая цифра, текущую вычитаем (IV = 5 - 1)
        if i + 1 < len(roman) and value < ROMAN_VALUES[roman[i + 1]]:
            result -= value
        else:
            result += value
    return result


print(from_roman("CMXC"))
