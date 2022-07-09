# 백준 1992 쿼드트리

import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
def abc(i, j, m):
    rst = arr[i][j]
    for a in range(i, i+m):
        for b in range(j, j+m):
            if rst == arr[a][b]:
                continue
            print('(', end="")
            abc(i, j, m//2)
            abc(i, j+m//2, m//2)
            abc(i+m//2, j+m//2, m//2)
            abc(i+m//2, j, m//2)
            print(')', end="")
            return
    if rst == 0:
        print('0', end="")
        return
    else:
        print("1", end="")
        return
abc(0, 0, n)

# 뭐가 틀렸을까?