# 백준 18868 멀티버스 I

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(M):
    for j in range(M):
        arr1 = sorted(arr[j])
        lst = []
        for k in arr[j]:
            lst.append(arr1.index(k)+1)
        arr[j] = lst
for a in range(M-1):
    for b in range(a+1, M):
        if arr[a] == arr[b]:
            ans += 1
print(ans)