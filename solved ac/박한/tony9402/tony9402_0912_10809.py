# 백준 10809 알파벳 찾기

import sys
input = sys.stdin.readline

lst = [-1]*26
S = list(input().strip())
for s in range(len(S)-1, -1, -1):
    a = S[s]
    lst[ord(a)-ord('a')] = s
print(*lst)