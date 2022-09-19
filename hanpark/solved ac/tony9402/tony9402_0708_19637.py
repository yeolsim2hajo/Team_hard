# 백준 19637 IF문 좀 대신 써줘

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst1, lst2 = ['none'], [-1]
for _ in range(n):
    lst = list(input().split())
    if len(lst2)==1 or int(lst[1]) != lst2[-1]:
        lst1.append(lst[0])
        lst2.append(int(lst[1]))
for _ in range(m):
    num = int(input())
    for i in range(n):
        if lst2[i] < num <= lst2[i+1]:
            print(lst1[i+1])
            break

# 시간 초과 고치려면 이분..?