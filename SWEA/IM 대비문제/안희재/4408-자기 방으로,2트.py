# 성공;; 피곤했나보다.. 이런걸 못보고
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    corridor = [0] * 200
    for i in range(N):
        if arr[i][0] > arr[i][1]:
            arr[i][0], arr[i][1] = arr[i][1], arr[i][0] # 30, 20인경우 -> 20, 30으로
        s = (arr[i][0] - 1) // 2 # index이므로 -1. no.1칸은 corridor의 0번칸
        e = (arr[i][1] - 1) // 2

        for j in range(s,e+1): # i번 학생이 지나는 모든 복도구간을 버킷에 표시해줌
            corridor[j] += 1

    print(f'#{tc}', max(corridor))
