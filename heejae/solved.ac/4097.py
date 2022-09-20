# 52112kb / 1080ms

# 구간합 논리와 비슷
import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    profit = []
    for i in range(N):
        profit.append(int(input()))

    # tmp -> 구간합
        # tmp의 3번째 인덱스는 3일까지의 수익의 합 / 5번인덱스 -> 5일까지 수익의 합
        # 점화식: tmp[3] = tmp[2] + profit[3]
    tmp = [0] * len(profit) # 구간합 tmp
    tmp[0] = profit[0] # 초기값 설정

    for i in range(1, len(profit)):
        tmp[i] = max(tmp[i - 1] + profit[i], profit[i])
        # 보통 상황에서, tmp[i]는 점화식대로 tmp[i-1] + profit[i] 로 정의한다.
        # 그러나, profit[i]가 더 크다면, tmp[i-1] 즉, tmp[i-1]까지의 합이 음수라는 뜻
        # -> tmp[i-1]을 버리고, tmp[i]는 profit[i](양수)로 바꿔줌
        # 이렇게 tmp 구간합 배열을 만들어 준 후 max(tmp) 출력

    print(max(tmp)) 
