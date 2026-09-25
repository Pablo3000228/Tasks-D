text = input("Введите текст: ").lower()
freq_symbols = {}
for el in text:
    count = text.count(el)
    freq_symbols[el] = count
s = sorted(freq_symbols, key=lambda x: freq_symbols[x], reverse=True)
for letter in freq_symbols:
    print(f"Кол-во элемента {letter}: {freq_symbols[letter]}")
print(s[:3])