# 2개의 음식을 만들지만, 각 음식을 만들 때 사용하는 재료의 개수는 N//2개
    # A와 B(A에 없는 재료들 모음)의 조합을 구한 다음에,
    # 일일이 각각의 A_sum,B_sum의 차이를 구한 후, 최솟값을 갱신시켜줌
    # 문제: N이 4일떄: A= (0,1) ... (2,3) / B= (2,3) ... (0,1)이다
        # 마지막 최솟값 구하는 코드에서 k=0과 마지막의 경우 사실상 같은 경우지만,
        # 이를 구별해주는 코드가 없다..
import sys
sys.stdin = open('cook_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = [0] * (N//2)
    A_food = []

    # dfs로 A_food의 재료 조합 만들기
    def dfs(level,start):
        if level == N//2:
            A_food.append(path[:])
            return

        for i in range(start,N):
            path[level] = i
            dfs(level+1,i+1)

    dfs(0,0)

    # 위에서 구한 A_food로 B_food의 재료 구할 수 있음(A에 없는것 = B의 재료)
    B_food = [[0]*(N//2) for _ in range(len(A_food))]
    for i in range(len(A_food)):
        idx = 0
        for j in range(N):
            if not j in A_food[i]:
                B_food[i][idx] = j
                idx += 1

    result = 2e18
    for k in range(len(A_food)): 
        A_sum, B_sum = 0, 0
        for i in range(N//2):
            for j in range(N//2):
                if i == j: continue # 0이니까
                A_sum += arr[A_food[k][i]][A_food[k][j]]
                B_sum += arr[B_food[k][i]][B_food[k][j]]
        if abs(A_sum-B_sum) < result:
            result = abs(A_sum-B_sum)

    print(f'#{tc}', result)