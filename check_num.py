number = int(input("Введите число: "))

if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")
if number > 0:
    print("Число положительное")
    if 10 <= number <= 50:
        print("Число принадлежит диапазону [10, 50]")
    else:
        print("Число не принадлежит диапазону [10, 50]")
elif number == 0:
    print("Число равно нулю")
else:
    print("Число отрицательное")