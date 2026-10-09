"""
Шифр Цезаря для русского и английского текста.

Сдвигает каждую букву на step позиций по алфавиту по кругу
(после последней буквы снова идёт первая). Регистр сохраняется,
пробелы, цифры и знаки препинания не меняются.

Input:
    lang - 1 (русский, 32 буквы без «ё») или 2 (английский, 26 букв);
    text - строка для обработки;
    func - 1 (зашифровать, сдвиг +step) или 2 (расшифровать, сдвиг -step).

Output:
    результат печатается в консоль.

Example (step = 3):
    "Hello, World!" -> "Khoor, Zruog!"
"""

step = int(input('Введите шаг: '))
lang = input("Выберите язык (1-русский, 2-английский): ")
text = input("Введите текст: ")

lang_len = 32 if lang == "1" else 26
first = "а" if lang == "1" else "a"

func = input("Что делаем? (1-расшифровываем, 2-дешифруем): ")
flag = True if func == "1" else False

res = ""

for el in text:
    if el.isalpha():
        f = first.upper() if el.isupper() else first
        i = ord(el) - ord(f)
        i = (i + step) % lang_len if flag else (i - step) % lang_len
        res += chr(i + ord(f))
    else:
        res += el
print(res)
