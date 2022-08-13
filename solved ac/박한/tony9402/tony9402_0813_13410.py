# 백준 13410 거꾸로 구구단
# 30840KB / 72ms

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ans = 0
for i in range(1, k+1):
    num, rst = str(n*i), ""
    m = len(num)
    for j in range(m):
        rst += num[m-1-j]
    ans = max(ans, int(rst))
print(ans)

# 간단하게 각 자리수를 나누서 str로 만든 것을 재조립하였음