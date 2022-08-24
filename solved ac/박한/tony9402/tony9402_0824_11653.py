# 백준 11653 소인수분해

import sys
input = sys.stdin.readline
n = int(input())
rst = 2
while n > 1:
    if n//rst == n/rst:
        print(rst)
        n = n//rst
    else:
        rst += 1