# 백준 20115 에너지 드링크

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
rst = max(lst) + sum(lst)
if rst/2 == rst//2:
    print(rst//2)
else:
    print(rst/2)