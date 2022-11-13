# 백준 10815 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

def binary(num):
    s, e = 0, n-1
    while s <= e :
        m = (s+e)//2
        if lst[m] == num :
            return 1
        elif lst[m] > num :
            e = m - 1
            # 반 줄여주기 1
        else:
            s = m + 1
            # 반 줄여주기 2
    return 0
a = input()
for l in list(map(int, input().split())):
    print(binary(l), end = ' ')