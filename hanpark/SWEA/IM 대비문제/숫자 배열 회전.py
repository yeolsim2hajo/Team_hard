T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst1 = ['']*N
    lst2 = ['']*N
    lst3 = ['']*N
    for i in range(N):
        for j in range(N):
            lst1[i] += str(arr[N-1-j][i])
            lst2[i] += str(arr[N-1-i][N-1-j])
            lst3[i] += str(arr[j][N-1-i])
    print(f"#{t+1}")
    for a in range(N):
        print(f"{lst1[a]} {lst2[a]} {lst3[a]}")