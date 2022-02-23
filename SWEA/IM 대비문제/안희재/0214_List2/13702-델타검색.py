for idx in range(1,11):
    N = int(input())
    arr = []
    for i in range(N):
        lst = list(map(int,input().split()))
        arr.append(lst)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def around_sum(x,y):
        sum = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                sum += abs(arr[x][y]-arr[nx][ny])
        return sum

    final_sum = 0
    for i in range(N):
        for j in range(N):
            final_sum += around_sum(i,j)

    print(f'#{idx} {final_sum}')
