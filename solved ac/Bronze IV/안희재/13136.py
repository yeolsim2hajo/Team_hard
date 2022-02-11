R, C, N = map(int, input().split())

row = 0
col = 0

if R % N == 0:
    row = R // N
else:
    row = R // N + 1

if C % N == 0:
    col = C // N
else:
    col = C // N + 1

print(row * col)