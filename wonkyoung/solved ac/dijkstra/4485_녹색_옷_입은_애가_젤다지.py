#221001
import sys, heapq
new_input = sys.stdin.readline

def find_loss(num):
    cave = [list(map(int, new_input().split())) for _ in range(num)]
    large_num = int(1e6)
    # 각 위치까지 잃는 최소 루피
    via_total = [[large_num]*num for _ in range(num)]
    # 각 위ㅊ
    min_total = [[large_num]*num for _ in range(num)]
    min_total[0][0] = cave[0][0]
    heap = []
    heapq.heappush(heap, (min_total[0][0], 0, 0))

    def target_loss(row, col):
        visited = [[large_num] * num for _ in range(num)]



    # 최단 거리
    while heap:
        loss, y, x = heapq.heappop(heap)
        for dy, dx in (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < num and 0 <= nx < num:
                min_total[ny][nx] = min(min_total[ny][nx], loss + min_total[y][x])
                heapq.heappush(heap, (target_loss(ny, nx), ny, nx))
    # 경유지 거친 거리
    for i in range(num):
        for j in range(num):
            target_loss(i, j)


    return min_total[num-1][num-1]

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    print(f'Problem {tc}: {find_loss(N)}')


