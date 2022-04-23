#75 이상한 369 - 다시
# number = int(input())
# number = number//3
# n = len(str(number))
# clap = 0
# for i in range(n-1,-1,-1):
#     # 숫자 앞에서부터
#     num = number%10
#     if num:
#         clap += (3**i)*num if num <= 3 else 3**(i+1)
#     number //= 10
# print(clap)


#77 가장 긴 공통 부분 문자열 - 다시


#78 원형테이블
# N, K = map(int,input().split())
# visited = [False]*(N)
# eat = idx = 0
# visited[0] = True
# leftover = N-1
# while leftover > 2:
#     if visited[idx] == False:
#         eat += 1
#         if eat == K:
#             eat = 0
#             visited[idx] = True
#             leftover -= 1
#     idx += 1
#     if idx == N:
#         idx = 0
# print([i+1 for i in range(N) if visited[i] == False])
