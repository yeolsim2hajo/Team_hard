# 백준 1145 적어도 대부분의 배수

import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
ans = min(lst)
while 1:
    rst = 0
    for i in range(5):
        if ans%lst[i] == 0:
            rst += 1
    if rst >= 3:
        print(ans)
        break
    ans += 1