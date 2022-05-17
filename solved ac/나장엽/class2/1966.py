import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    importances = list(map(int, input().split()))
    printed = []
    i = 0
    lenth = len(importances)
    
    while m not in printed:
        imp = importances[i]
        if imp >= max(importances):
            if i==m:
                print(len(printed)+1)
                break
            printed.append(i)
            importances[i] = -1
        i = (i + 1) % lenth