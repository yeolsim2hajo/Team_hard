# 백준 class 3++ 11403 경로 찾기

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for a in range(n):
    for b in range(n):
        for c in range(n):
            if arr[a][c] == 0 or arr[b][a] == 0:
                if arr[b][c] == 0:
                    continue
            arr[b][c] = 1

for i in range(n):
    print(* arr[i])