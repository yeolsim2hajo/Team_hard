# 백준 14425 문자열 집합

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    a = str(input())
    dic[a] = 1
ans = 0
for _ in range(m):
    b = str(input())
    if b in dic.keys():
        ans += 1
print(ans)