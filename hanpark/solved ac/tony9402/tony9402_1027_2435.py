# 백준 2435 기상청 인턴 신현수

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
for i in range(n-k+1):
    rst = 0
    for j in range(i, i+k):
        rst += lst[j]
    ans.append(rst)
print(max(ans))