T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # N은 사람 수, M초에 K개를 만들 수 있음
    times = list(map(int,input().split()))

    # 일단, 도착하는 사람들의 시간 sort로 정렬
    times.sort()

    # times 첫 손님이 일단 M보다 작으면 무조건 impossible
    result = 'Possible'
    s = 0 # 인덱스, 처리한 인원수
    cnt = 1 # 0초
    while s < N:
        if times[s] >= M*cnt: # start!
            s += K
            cnt += 1
        else:
            result = 'Impossible'
            break

    print(f'#{tc}', result)

# 페어 코드
# -------------------------------------------
# T = int(input())
# for test_case in range(1, T + 1):
#     n, m, k = map(int, input().split())
#     arrive = sorted(list(map(int, input().split())))
#     answer = 'Possible'
#     for i in range(len(arrive)):
#         time = arrive[i]
#         cnt = (time//m)*k - i
#         if cnt < 1:
#             answer = 'Impossible'
#
#     print(f'#{test_case} {answer}')
# arrive = [3,3,3,3,3,5,6]의 경우 : 4번째 인덱스에서 컷당함!  
# 어우 이 논리도 되게 좋네.. 처음 생각하는게 좀 힘들긴 할듯..
# -------------------------------------------