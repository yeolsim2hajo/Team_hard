# 백준 10808 알파벳 개수

import sys
input = sys.stdin.readline
S = input().strip()
lst = [0]*26
for s in S:
    lst[ord(s)-ord('a')] += 1
print(*lst)