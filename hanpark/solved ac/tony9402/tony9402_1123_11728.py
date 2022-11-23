# tony9402 11728 배열 합치기

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
ans = a+b
ans.sort()
print(*ans)