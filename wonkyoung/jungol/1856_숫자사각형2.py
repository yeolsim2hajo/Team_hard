#221116
N, M = map(int, input().split())
for i in range(N):
    if i%2 == 0:
        print(*list(range(M*i+1, M*(i+1)+1)))
    else:
        print(*list(range(M * (i+1), M * i, -1)))
