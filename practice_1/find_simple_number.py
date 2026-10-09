N = int(input())

a = [1] * N

a[0] = 0
a[1] = 0

for i in range(2, int(N ** 0.5) + 1):
    if a[i] == 1:
        for j in range(i * i, N, i):
            a[j] = 0

for i in range(2, N):
    if a[i] == 1:
        print(i, end=' ')