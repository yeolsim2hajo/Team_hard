#221001
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    new = [list(map(int, input().split())) for _ in range(N)]
    min_fuel = 1e6
    result = [[min_fuel] * N for _ in range(N)]
    result[0][0] = 0

    print(f'#{tc} {min_fuel}')

