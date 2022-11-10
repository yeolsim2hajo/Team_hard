N, M = map(int, input().split())
for i in range(N):
    print(*range(M*i + 1, M*(i+1) + 1))