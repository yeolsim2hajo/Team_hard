# 백준 16171 나는 친구가 적다(small)

import sys
input = sys.stdin.readline

s = input()
k = input()
lst = ''
for i in s:
    if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
        lst += i
if lst.find(k) != -1:
    print(1)
else:
    print(0)