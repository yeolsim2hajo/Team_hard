# 돈을 가장 많이 번 구간이 언제인지?
while True:
    # 데이터 입력
    N = int(input())
    # 종료 조건
    if N == 0:
        break

    # 초기화
    earning = [int(input()) for _ in range(N)]
    # -----------------------------------------------------------------
    # # 구간 check, max값 갱신 -> 시간초과
    # for i in range(len(earning)):
    #     temp = 0
    #     for k in range(i, len(earning)): # 0 ~ 6, 1 ~ 6, 2 ~ 6, 3 ~ 6
    #         temp +=  earning[k]
    #     # 구간마다 max값 갱신
    #     max_earning = max(temp, max_earning)
    # ------------------------------------------------------------------
    # 누적합, 해당 인덱스의 값과, 구간의 합을 구하여 max 비교 -> 인덱스 값 갱신 -> 배열의 max값 print
    for index in range(1, N):
        earning[index] = max(earning[index], earning[index] + earning[index - 1]) 
    print(max(earning))
