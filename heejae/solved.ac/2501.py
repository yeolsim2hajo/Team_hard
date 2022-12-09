import math
N = int(input())
cnt = 0
for i in range(1, int(math.sqrt(N)) + 1):
    if N == i * i:
        cnt += 1
        continue
    if N % i == 0:
        cnt += 2

print(cnt)