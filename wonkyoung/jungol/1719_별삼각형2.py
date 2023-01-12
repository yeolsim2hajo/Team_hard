#221116
N, M = map(int, input().split())
half = N//2 + 1

for i in range(1, half):
    print('*' * i)
for i in range(half, 0, -1):
    print('*' * i)