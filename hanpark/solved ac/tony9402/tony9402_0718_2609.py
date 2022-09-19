# 백준 2606 바이러스

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
check = [0]*n
arr = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1], arr[b-1][a-1] = 1, 1

def abc(a):
    for i in range(n):
        if arr[a][i] == 1 and check[i] == 0:
            check[i] = 1
            abc(i)

abc(0)
print(sum(check)-1)  # 1은 카운트하지 않으니까