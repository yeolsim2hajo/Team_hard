# 백준 6603 로또

import sys
import itertools
input = sys.stdin.readline

while 1:
    lst = list(map(int, input().split()))
    n = lst[0]
    ls = lst[1:]
    for l in itertools.combinations(ls, 6):
        print(*l)
    if n == 0:
        exit()
    print()