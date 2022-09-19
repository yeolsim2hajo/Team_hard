T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr1 = [[0]*(N+2) for _ in range(N+2)]
    arr2 = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            arr1[i+1][j+1] = arr[i][j]
            arr2[i+1][j+1] = arr[j][i]
    def get_a(ar, n, k):
        ans = 0
        for i in range(1, n+1):
            for a in range(1, n-k+2):
                rst = 0
                for b in range(k):
                    if ar[i][a+b] == 1:
                        rst += 1
                if rst==k and ar[i][a-1]==0 and ar[i][a+k]==0:
                    ans += 1
        return ans
    res = get_a(arr1, N, K)+get_a(arr2, N, K)
    print(f"#{t+1} {res}")