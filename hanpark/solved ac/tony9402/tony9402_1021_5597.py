# 백준 5597 과제 안 내신 분...?

import sys
input = sys.stdin.readline
lst = [i for i in range(1, 31)]
for _ in range(28):
    n = int(input())
    lst.remove(n)
print(min(lst))
print(max(lst))