# 백준 1268 임시 반장 정하기

import sys
input = sys.stdin.readline

T = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(T)]
lst = [0]*T
for t in range(T):
    visit = [0]*T
    for a in range(5):
        for b in range(T):
            if b != t and arr[b][a] == arr[t][a]:
                visit[b] = 1
    lst[t] = len(list(filter(lambda x: x, visit)))

print(lst.index(max(lst))+1)