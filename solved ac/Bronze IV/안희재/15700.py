N, M = map(int,input().split())

if N % 2:
    print(N//2 * M + M // 2)
else:
    print(N//2 * M)