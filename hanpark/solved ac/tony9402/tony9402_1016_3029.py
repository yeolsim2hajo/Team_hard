# 백준 3029 경고

import sys
input = sys.stdin.readline

ta = list(map(int, input().split(':')))
tb = list(map(int, input().split(':')))
A, B = ta[0]*3600 + ta[1]*60 + ta[2], tb[0]*3600 + tb[1]*60 + tb[2]
if A < B:
    ans = B-A
else:
    ans = B-A+86400
lst = [ans//3600, (ans%3600)//60, (ans%3600)%60]
for i in range(3):
    if lst[i] < 10:
        lst[i] = "0" + str(lst[i])
    else:
        lst[i] = str(lst[i])
print(f"{lst[0]}:{lst[1]}:{lst[2]}")