"""Генератор паролей с настройками.

Программа спрашивает у пользователя параметры пароля (регистр букв,
спецсимволы, цифры, длину) и генерирует пароли по этим настройкам.
Настройки можно поменять, не перезапуская программу.
"""

import secrets

specials = "!@#$%^&*_+-="
nums = "0123456789"
l_letters = "abcdefghijklmnopqrstuvwxyz"
u_letters = l_letters.upper()

GREEN = "\033[32m"
RESET = "\033[0m"
LINE = "-" * 40


def ask(question, options):
    """
    Задаёт вопрос, пока пользователь не введёт допустимый ответ.

    Parameters:
        question (str): Текст вопроса,
        options (list): Список допустимых ответов.

    Returns:
        str: Ответ пользователя из списка options.
    """

    while True:
        answer = input(question).strip()
        if answer in options:
            return answer
        print("  Нет такого варианта, попробуйте ещё раз.")


def ask_length():
    """
    Спрашивает длину пароля от 4 до 64.

    Returns:
        int: Длина пароля.
    """

    while True:
        answer = input("Длина пароля (4-64): ").strip()
        if answer.isdigit() and 4 <= int(answer) <= 64:
            return int(answer)
        print("  Введите число от 4 до 64.")


def settings():
    """
    Спрашивает у пользователя настройки пароля.

    Returns:
        list: Список настроек [case, spec, numbers, length], где
            case (str) — регистр ("1" - верхний, "2" - нижний, "3" - оба),
            spec (str) — спецсимволы ("1" - да, "2" - нет),
            numbers (str) — цифры ("1" - да, "2" - нет),
            length (int) — длина пароля.
    """

    print(f"\n{LINE}\n  Настройка\n{LINE}")
    case = ask("Регистр (1 - верхний, 2 - нижний, 3 - оба): ", ["1", "2", "3"])
    spec = ask("Спецсимволы (1 - да, 2 - нет): ", ["1", "2"])
    numbers = ask("Цифры (1 - да, 2 - нет): ", ["1", "2"])
    length = ask_length()
    return [case, spec, numbers, length]


def show_settings(choice):
    """
    Печатает текущие настройки пароля.

    Parameters:
        choice (list): Список настроек.
    """

    case, spec, numbers, length = choice
    cases = {"1": "верхний", "2": "нижний", "3": "оба"}
    yes_no = {"1": "да", "2": "нет"}
    print(
        f"\nРегистр: {cases[case]} | Спецсимволы: {yes_no[spec]} | "
        f"Цифры: {yes_no[numbers]} | Длина: {length}"
    )


def generate(choice):
    """
    Генерирует пароль по заданным настройкам.

    Parameters:
        choice (list): Список настроек.

    Returns:
        str: Сгенерированный пароль.
    """

    case, spec, numbers, length = choice

    chars = ""
    if case == "1":
        chars += u_letters
    elif case == "2":
        chars += l_letters
    else:
        chars += l_letters + u_letters

    if spec == "1":
        chars += specials
    if numbers == "1":
        chars += nums

    password = ""
    for _ in range(length):
        password += secrets.choice(chars)

    return password


print(LINE)
print("  Генератор паролей с настройками")
print(LINE)

choice = settings()

while True:
    show_settings(choice)
    print(f"\n  Ваш пароль:  {GREEN}{generate(choice)}{RESET}\n")
    print(LINE)

    action = ask("1 - ещё пароль, 2 - изменить настройки, 3 - выход: ", ["1", "2", "3"])
    if action == "2":
        choice = settings()
    elif action == "3":
        print("\nДо свидания!\n")
        break
