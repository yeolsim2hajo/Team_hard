# 백준 1110 더하기 사이클

import sys
input = sys.stdin.readline

N = int(input())
rst, ans = (N%10 * 10) + (N//10 + N%10)%10, 1
while rst != N:
    check = (rst//10 + rst%10)%10
    rst = (rst%10 *10) + check
    ans += 1
print(ans)