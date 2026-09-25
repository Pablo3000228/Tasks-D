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

print(str(number)[digit])

# Советовался с ИИ по пути решения