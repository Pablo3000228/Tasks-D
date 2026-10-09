N = int(input())

length = 1
count = 9
start = 1

while N > length * count:
    N -= length * count
    length += 1
    count *= 10
    start *= 10

number = start + (N - 1) // length
digit = (N - 1) % length

<<<<<<< HEAD:Task 6.py
print(str(number)[digit])
=======
print(str(number)[digit])
>>>>>>> 503b772 (Calc & Practice #2):practice_1/Task 6.py
