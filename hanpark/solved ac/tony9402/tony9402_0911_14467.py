# 백준 14467 소가 길을 건너간 이유 1

import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
rst = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = b
    else:
        if dic[a] != b:
            dic[a] = b
            rst += 1
print(rst)