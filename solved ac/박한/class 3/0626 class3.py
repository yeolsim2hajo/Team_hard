# 백준 1764 듣보잡

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst1 = [input() for _ in range(n)]
lst2 = [input() for _ in range(m)]
lst1.sort()
lst2.sort()
lst = []
rst1,rst2 = 0, 0
while rst1 < n:
    check = 0
    for i in range(rst1, n):
        if check != 0:
            break
        for j in range(rst2, m):
            if lst1[i] == lst2[j]:
                lst.append(lst1[i])
                check = 1
                rst1, rst2 = i+1, j+1
                break
    if check == 0 or rst2 >= m:
        break

ans = len(lst)
print(ans)
for i in range(ans):
    print(lst[i])