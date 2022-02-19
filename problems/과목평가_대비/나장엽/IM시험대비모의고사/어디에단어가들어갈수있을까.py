T = int(input())
# 0 1 1 1 0
# 0 0 1 1 1 
# 1 1 1 0 0 
# ! 미완성 코드입니다 !
# ! 다시 풀어보기  !
def find_location(n, k, arr):
    result = 0
    #행 방향 탐색
    for i in range(n):
        cnt = 0
        for k in range(n):
            if arr[i][k] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
    #열 방향 탐색
    for i in range(n):
        cnt = 0
        for k in range(n):
            if arr[][k] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0

for tc in range(1, T+1):
    n = int(input)
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    