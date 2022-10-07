# 백준 10448 유레카 이론

import sys
input = sys.stdin.readline

def find(n):
    for i in range(len(t)):
        for j in range(i,len(t)):
            for k in range(j,len(t)):
                if t[i]+t[j]+t[k] == n:
                    return 1
    return 0
    
t = [1]
for i in range(2,45):
    t.append(t[-1]+i)
for _ in range(int(input())):
    n = int(input())
    print(find(n))