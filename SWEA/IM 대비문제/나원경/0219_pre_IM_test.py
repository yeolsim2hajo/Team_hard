# 진기의 붕어빵
# import sys
# sys.stdin = open("input(5).txt", "r")
# def is_possible(time_arr,people,time,number):
#     max_cnt = 0 # 도착 시간 개수를 셀 cnt 배열의 크기 결정
#     for i in range(people):
#         if time_arr[i] < time: # 만드는 데 드는 시간보다 일찍 도착
#             return 'Impossible'
#         if max_cnt < time_arr[i]:
#             max_cnt = time_arr[i]
#     cnt = [0]*(max_cnt+1) # 도착 시간 개수 세는 배열
#     for i in range(people):
#         cnt[time_arr[i]] += 1
#     order = 0 # 이전 주문 수
#     for i in range(max_cnt+1):
#         if cnt[i]:
#             left = (i//time) * number - order
#             order += 1
#             if left <= 0:
#                 return 'Impossible'
#     else: return 'Possible'
#
# T = int(input())
# for tc in range(1,T+1): # 사람 수, 시간, 개수
#     n, m, k = map(int, input().split())
#     arrive = [int(x) for x in input().split()]
#     print('#{}'.format(tc), end=' ')
#     print(is_possible(arrive,n,m,k))

# 자기 방으로 돌아가기

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    now = [0] * n
    room = [0] * n
    for i in range(n):
        now[i], room[i] = map(int,input().split())
    time = 1
    cnt = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and (now[i] <= now[j] <= room[i] or now[i] <= room[j] <= room[i]):
                cnt[i] += 1
                


    print(cnt)
    print(f'#{tc} {time}')
