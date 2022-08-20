# 민호쌤..
import math

N, M, R = map(int, input().split())

NUMBERS = [list(map(int, input().split())) for _ in range(N)]

turns = []
for k in range(min(N, M)//2):
    turns.append(2*((N-(2*k))+(M-(2*k)))-4)


for k in range(min(N,M)//2):
    for r in range(R%turns[k]):
        temp = NUMBERS[k][k]
        for i in range(1+k, M-k):
            NUMBERS[k][i-1] = NUMBERS[k][i]

        for i in range(1+k, N-k):
            NUMBERS[i-1][M-1-k] = NUMBERS[i][M-1-k]

        for i in range(1+k, M-k):
            NUMBERS[N-1-k][M-i]=NUMBERS[N-1-k][M-1-i]

        for i in range(1+k, N-k):
            NUMBERS[N-i][k] = NUMBERS[N-1-i][k]

        NUMBERS[1+k][k] = temp

for n in NUMBERS:
    print(" ".join(map(str,n)))