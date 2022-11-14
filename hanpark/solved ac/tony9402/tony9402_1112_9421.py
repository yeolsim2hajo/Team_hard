# 백준 9421 소수상근수

import sys
input = sys.stdin.readline

n = int(input())
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
lst=[]
for i in primes:
    visited=dict()
    temp=str(i)
    while True:
        tmp=sum(map(lambda x:int(x)**2,temp))
        idx=int(temp)
        if tmp==1:
            lst.append(i)
            break
        if visited.get(idx):
            break
        else:
            visited[idx]=1
        temp=str(tmp)
lst.sort()
for l in lst:
    print(l)