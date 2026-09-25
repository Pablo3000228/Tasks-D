text = input("Введите текст: ").lower()
max = 0
freq_symbols = {}
for el in text:
    count = text.count(el)
    freq_symbols[el] = count
s = sorted(freq_symbols, key=lambda x: freq_symbols[x], reverse=True)
print(s[:3])
    