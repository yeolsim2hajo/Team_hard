# 백준 5618 공약수

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().strip().split()))
ans = []
for i in range (1,min(lst)+1):
    if n==2:
        if lst[0]%i==0 and lst[1]%i==0:
            ans.append(i)
    elif n==3:
        if lst[0]%i==0 and lst[1]%i==0 and lst[2]%i==0:
            ans.append(i)
            

for i in ans:
    print(i) 