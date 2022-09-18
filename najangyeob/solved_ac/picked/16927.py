# 풀이
# layer 별로 분리해서 만들고, 출력
# 바깥 ~ 안쪽으로 layer 분리 -> 분리한 것을 1차원 배열로 보면, 왼쪽으로 R만큼 이동한다.
# n, m의 값 비교, 짝수, 홀수인 경우로 분리
#


import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

layers = []
smaller = N if N < M else M
layer = smaller // 2
# 짝수
if smaller % 2 == 0:
    # 배열 생성
    for l in range(layer):
        # top
        tmp = matrix[l][l:M - l]
        # right
        for right in range(N - 2 - l*2):
            tmp.append(matrix[right + l + 1][M - 1 - l])
        # bottom
        tmp += list(reversed(matrix[N - 1 - l][l:M - l]))
        # left
        for left in range(N - 2 - l * 2):
            tmp.append(matrix[N - 1 - (l+1) - left][l])
        layers.append(tmp)
# 홀수
else: 
    #  배열 생성
    for l in range(layer):
        # top
        tmp = matrix[l][l:M - l]
        # right
        for right in range(N - 2 - l * 2):
            tmp.append(matrix[right + 1][M - 1 - l])
        # bottom
        tmp += list(reversed(matrix[N - 1 - l][l:M - l]))
        # left
        for left in range(N - 2 - l * 2):
            tmp.append(matrix[N - 1 - left - 1][l])
        layers.append(tmp)

    # layer 만큼만 추가, 가장 안쪽 넣기
    tmp = []
    if smaller == N:
        for col in range(M - 2 * layer):
            tmp.append(matrix[smaller // 2][layer + col])
    else:
        for row in range(N - 2 * layer):
            tmp.append(matrix[layer + row][smaller // 2])
    layers.append(tmp)

# rotate
new_layers = []
for l in range(layer):
    if len(layers[l]) > R:
        new_layers.append(layers[l][R:] + layers[l][0:R])
    else:
        tmp_rotate_cnt = R % len(layers[l])
        new_layers.append(layers[l][tmp_rotate_cnt:] + layers[l][0:tmp_rotate_cnt])
if smaller % 2 == 1:
    new_layers.append(layers[-1])

# rollback
new_matrix = []

for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append(0)
    new_matrix.append(tmp)

for l in range(layer):
    # top
    for i in range(M - l*2):
        new_matrix[l][i + l] = new_layers[l][i]
    # right
    for right in range(N - 2 - l*2):
        new_matrix[l + 1 + right][M - 1 - l] = new_layers[l][(M - l*2) + right]
    # bottom 
    start_idx = len(new_layers[l]) // 2
    for col in range(M - l*2):
        new_matrix[N - 1 - l][M - 1 - l - col] = new_layers[l][start_idx + col]
    # left 
    for left in range(N - 2 - l*2):
        new_matrix[l + 1 + left][l] = new_layers[l][-(left + 1)]

if smaller % 2 == 1: 
    if smaller == N:
        for i in range(M - layer*2):
            new_matrix[N//2][layer + i] = new_layers[-1][i]
    else:
        for j in range(N - layer*2):
            new_matrix[M//2][layer + j] = new_layers[-1][i]

# 출력            
for row in new_matrix:
    print(*row)