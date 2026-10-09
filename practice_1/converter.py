celsius = float(input("Введите температуру в Цельсиях: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit:.2f}°F")
print(f"{celsius}°C = {kelvin:.2f}K")