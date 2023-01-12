N, L, D = map(int, input().split())
end_time = 0
for i in range(N):
    if i*L + 5*(i-1) <= D <= i*L + 5*i:
        pass