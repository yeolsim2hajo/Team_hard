# 백준 11655 ROT13

import sys
input = sys.stdin.readline
lst = list(input())
for a in range(len(lst)):
    if (ord('a') <= ord(lst[a]) <= ord('m')) or (ord('A') <= ord(lst[a]) <= ord('M')):
        lst[a] = chr(ord(lst[a])+13)
    elif (ord('n') <= ord(lst[a]) <= ord('z')) or (ord('N') <= ord(lst[a]) <= ord('Z')):
        lst[a] = chr(ord(lst[a])-13)
    print(lst[a], end="")