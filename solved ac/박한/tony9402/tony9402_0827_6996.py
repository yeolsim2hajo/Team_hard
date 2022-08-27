# 백준 6996 애너그램

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    A, B = list(a), list(b)
    if sorted(A) == sorted(B):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")