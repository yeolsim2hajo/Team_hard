# 백준 1342 행운의 문자열

import sys
input = sys.stdin.readline
S = input().strip()
lst = [0]*26
ans = 0
for s in S:
    lst[ord(s)-ord('a')] += 1
def abc(a, b):
    global ans
    if a == 0:
        ans += 1
        return
    for s in S:
        if s == b:
            continue
        if lst[ord(s)-ord('a')] > 0:
            lst[ord(s)-ord('a')] -= 1
            abc(a-1, s)
            lst[ord(s)-ord('a')] += 1
abc(len(S), '')
print(ans)

# 디버깅 못하게슴..