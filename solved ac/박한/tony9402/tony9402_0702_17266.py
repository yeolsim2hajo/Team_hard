# 백준 17266 어두운 굴다리

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
lst = list(map(int, input().split()))
ans = max(lst[0], n-lst[-1])
if m > 1:
    for i in range(m-1):
        rst = round((lst[i+1]-lst[i])/2)
        ans = max(rst, ans)
print(ans)