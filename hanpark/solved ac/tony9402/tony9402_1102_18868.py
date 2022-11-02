# 백준 18868 멀티버스 Ⅰ

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for j in range(m):
        arr_sort = sorted(arr[j])  # 정렬 먼저 해준 후
        lst = []
        for k in arr[j]:  # 크기 순으로 인덱스 순서 리스트 만들기
            lst.append(arr_sort.index(k) + 1)
        arr[j] = lst
ans = 0
for i in range(m-1):
    for j in range(i+1, m):
        if arr[i] == arr[j]:  # 우주끼리 리스트 순서가 같으면 cnt++
            ans += 1
print(ans)