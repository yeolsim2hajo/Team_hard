# 백준 21312 홀짝 칵테일

import sys
input = sys.stdin.readline

lst = list(map(int, input().strip().split()))
rst = 1
if lst[0]%2==0 and lst[1]%2==0 and lst[2]%2==0:
    rst = lst[0]*lst[1]*lst[2]
else:
    for n in lst:
        if n%2==1:
            rst *= n
print(rst)