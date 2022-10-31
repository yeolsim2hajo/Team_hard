# 백준 14405 피카츄

from re import S
import sys
input = sys.stdin.readline

S = input()
lst = ['pi', 'ka', 'chu']
for a in lst:
    S = S.replace(a, '')
for s in S:
    if ord('a') <= ord(s) <= ord('z'):
        print("NO")
        break
    else:
        print("YES")