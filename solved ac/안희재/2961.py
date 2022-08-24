import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

com = []
for i in range(1, N+1):
    com.append(combinations(arr, i))

answer = 1000000000
for line in com:
    for each in line:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]

        answer = min(answer, abs(sour - bitter))

print(answer)