# 백준 1032 명령 프롬프트

import sys
input = sys.stdin.readline

N = int(input())
a = list(input().strip())
for _ in range(N-1):
    b = list(input().strip())
    for n in range(len(a)):
        if a[n] != b[n]:
            a[n] = '?'
for i in range(len(a)):
    print(a[i], end="")