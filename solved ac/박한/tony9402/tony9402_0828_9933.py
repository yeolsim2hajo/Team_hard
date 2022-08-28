# 백준 9933 민균이의 비밀번호

import sys
input = sys.stdin.readline
n = int(input())
lst = [input().strip() for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if len(lst[i]) == len(lst[j]) and lst[i][::-1] == lst[j]:
            print(f"{len(lst[i])} {lst[i][int(len(lst[i])/2)]}")