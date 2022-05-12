#2798 블랙잭
# N, M = map(int,input().split())
# cards = list(map(int,input().split()))
# answer = 0
# def dfs(start=0,arg=0, total=0):
#     global answer
#     if total > M:
#         return
#     if arg == 3:
#         if total > answer:
#             answer = total
#         return
#     for i in range(start,N):
#         dfs(i+1,arg+1,total+cards[i])
# dfs()
# print(answer)


#2805 나무 자르기 - 수정 필요
# N, M = map(int,input().split())
# heights = list(map(int,input().split()))
# heights.sort(reverse=True)
# max_height = heights[-1]
# answer = sum(heights) - max_height * N
# 
# if answer > M: # max_height 증가시켜야 함
#     N -= 1
#     while True:
#         max_height += 1
#         answer -= N
#         if answer == M:
#             print(max_height)
#             break
#         else:
#             if answer < M:
#                 print(max_height+1)
#                 break
#             if heights[N-1] == max_height:
#                 N -= 1
#                 max_height = heights[N-1]
#                 if answer == M:
#                     print(max_height)
#                     break
# 
# elif answer < M: # max_height 감소시켜야 함
#     while True:
#         max_height -= 1
#         answer += N
#         if answer == M:
#             print(max_height)
#             break
#         elif answer > M:
#             print(max_height - 1)
#             break
# else:
#     print(max_height)