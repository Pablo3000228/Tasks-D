def add_numbers(a: float, b: float) -> float:
    """
    Расчитывает сумму двух чисел.

    Args:
        a (float) - первое число
        b (float) - второе число.

    Returns:
        float: Итоговая сумма

    Example:
        >>> add_numbers(2, 3)
        5
    """

    return a + b


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2, 0) == 2


test_add_numbers()

print(add_numbers(2, 4))
