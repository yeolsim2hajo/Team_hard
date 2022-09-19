T = int(input())
# 테스트케이스 개수
for t in range(T):
    N = int(input())
    # N - 방에 돌아가야 할 학생의 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [0]*200
    # 각 복도를 칸으로 표현해서 200개의 칸으로 표현할 수 있음
    # 큰 짝수와 작은 홀수 사이에선 칸을 i개 먹지만 작은 짝와 큰 홀수 사이에선 i+1개 먹음
    # 이를 홀수면 i//2 + 1, 짝수면 i/2로 만들어 표현할 수 있을 듯?
    # 그냥 같은 방으로 묶으면 4-6, 7-8 같은 케이스 여전히 커버 불가능
    arr1 = [[0, 0] for _ in range(N)]
    for i in range(N):
        for j in range(2):
            if arr[i][j]%2==1:
                arr1[i][j] = arr[i][j]//2 + 1
            else:
                arr1[i][j] = arr[i][j]//2
    for n in range(N):
        if arr1[n][0] > arr1[n][1]:
            for i in range(arr1[n][1], arr1[n][0]+1):
                lst[i] += 1
        else:
            for j in range(arr1[n][0], arr1[n][1]+1):
                lst[j] += 1
    for a in range(200):
        for b in range(a+1, 200):
            if lst[a] < lst[b]:
                lst[a], lst[b] = lst[b], lst[a]
    rst = lst[0]
    print(f"#{t+1} {lst[0]}")
    # 1-4, 3-6은 안되는데 1-3 4-6은 되는 거아님? 2-4 3-5는 어떤대? 개오바네