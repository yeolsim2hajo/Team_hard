#221028
N, M = map(int, input().split())
rectangular = [input() for _ in range(N)]
max_len = 1
limit = min(N, M)
for i in range(N-1):
    for j in range(M-1):
        for k in range(1, limit):
            if i+k >= N or j+k >= M:
                break
            number = rectangular[i][j]
            for di, dj in (k, 0), (0, k), (k, k):
                if rectangular[i+di][j+dj] != number:
                    break
            else:
                max_len = max(max_len, k+1)
print(max_len ** 2)

