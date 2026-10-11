def print_pack_report(cnt: int) -> None:
    """
    Печатает, как расфасовать пирожные по 3 или по 5 штук.

    Parameters:
        cnt: количество пирожных, целое число больше 1
    """

    for i in range(cnt, 0, -1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 5 == 0 and i % 3 != 0:
            print(f"{i} - расфасуем по 5")
        elif i % 3 == 0 and i % 5 != 0:
            print(f"{i} - расфасуем по 3")
        else:
            print(f"{i} - не заказываем!")
