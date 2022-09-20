import sys
input = sys.stdin.readline
p, k = map(int, input().split())
e = [0 for i in range(1000001)]
result = 0
for i in range(2, 1001):
    if e[i] == 0:
        n = i * 2
        while n < 1000001:
            e[n] = 1
            n += i
for i in range(2, 1000001):
    if e[i] == 0:
        if p % i == 0:
            result = i
            break
if result == 0: print("GOOD")
else:
    if result < k: print("BAD", result)
    else: print("GOOD")