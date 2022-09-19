# 거꾸로
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# score = [int(new_input()) for _ in range(N)]
# step, cnt = N-1, 1
# max_score = score[step]
# while step > 1:
#     if cnt and score[step-1] > score[step-2]:
#         step -= 1
#         cnt -= 1
#     else:
#         cnt = 1
#         step -= 2
#     max_score += score[step]
# if step and cnt:
#     max_score += score[step-1]
# print(max_score)

'''
9
40
25
50
80
100
10
20
25
75

'''

#17212 달나라 토끼를 위한 구매대금 지불 도우미
# price = int(input())
# min_cnt = price
# seven, remain = divmod(price, 7)
# for i in range(seven,-1,-1):
#     five, remain = divmod(remain, 5)
#     for j in range(five, -1, -1):
#         two, remain = divmod(remain, 2)
#         min_cnt = min(min_cnt, remain+i+j+two)
#         remain = price - 7*i - 5*(j-1)
#     remain = price - 7*(i-1)
# print(min_cnt)



#17390 이건 꼭 풀어야 해!
# import sys
#
# new_input = sys.stdin.readline
# N, Q = map(int, new_input().split())
# arr = sorted((map(int, new_input().split())))
# acc = [0]
# for i in range(N):
#     acc.append(acc[i] + arr[i])
# for _ in range(Q):
#     start, end = map(int, new_input().split())
#     print(acc[end] - acc[start-1])


# import sys
#
# new_input = sys.stdin.readline
# N, Q = map(int, new_input().split())
# arr = [0] + sorted((map(int, new_input().split())))
# for i in range(1,N+1):
#     arr[i] += arr[i-1]
# for _ in range(Q):
#     start, end = map(int, new_input().split())
#     print(arr[end] - arr[start-1])



# import sys
#
# new_input = sys.stdin.readline
# N, Q = map(int, new_input().split())
# arr = sorted((map(int, new_input().split())))
# for i in range(1,N):
#     arr[i] += arr[i-1]
# for _ in range(Q):
#     start, end = map(int, new_input().split())
#     if start == 1:
#         print(arr[end-1])
#     else:
#         print(arr[end-1] - arr[start-2])