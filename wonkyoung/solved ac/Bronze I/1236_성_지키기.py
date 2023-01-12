#221229
N, M = map(int, input().split())
castle = [input() for _ in range(N)]
if N >= M:
    cnt = max_num = N
    min_num = M
else:
    cnt = max_num = M
    min_num = N
for i in range(max_num):
    for j in range(max_num):
        if i < M:
            pass
                            