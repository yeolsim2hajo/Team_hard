# 못 품 -> 및 이 풀이는 시간 오래 걸림 -> 다시
# 32884kb / 4104ms
import sys

N, M, R = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

# 한바퀴 회전
def rotate(i, j, n, m):
    top = array[i][j]
    left = array[n - 1][j]
    bottom = array[n - 1][m - 1]
    right = array[i][m - 1]

    for x in range(n-1, i, -1):                 # left
        array[x][j] = array[x-1][j]
    for x in range(i, n-1):                     # right
        array[x][m - 1] = array[x+1][m - 1]
    for y in range(j, m - 1):                   # top
        array[i][y] = array[i][y + 1]
    for y in range(m-1, j, -1):                 # bottom
        array[n - 1][y] = array[n - 1][y-1]
    array[i+1][j] = top
    array[n-1][j+1] = left
    array[n-2][m-1] = bottom
    array[i][m-2] = right

    # 1 2 3 4  => 왼쪽으로 미루게 되면, 2 3 4 1  -> 맨 오른쪽 자리는 

deep = min(N, M) // 2  					# 몇번이나 안쪽으로 들어가는지?
cycle = (N - 1) * 2 + (M - 1) * 2  		# 4x4 경우, 둘레 = 12 -> 12번 돌면 원상복구

for i in range(deep): 					# 겉 - 안쪽 - 안쪽 ... 순으로
    for _ in range(R % cycle):			# 회전 횟수 압축
        rotate(i, i, N - i, M - i)
    cycle -= 8  						# 겉과 안쪽의 둘레 차 (규칙적으로 -8) = 8칸 차이

for x in array:
    print(*x, sep=' ')