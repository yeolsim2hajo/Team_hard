#20116 상자의 균형
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# total = sum(center)
# for i in range(N-1):
#     total -= center[i]
#     if not(center[i] - L < total/(N-i-1) < center[i] + L):
#         print('unstable')
#         break
# else:
#     print('stable')


# 거꾸로
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# total = center[-1]
# for i in range(N-2,-1,-1):
#     if not(center[i] - L < total/(N-i-1) < center[i] + L):
#         print('unstable')
#         break
#     total += center[i]
# else:
#     print('stable')

# 시간 더 걸림
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# total = center[-1]
# for i in range(N-2,-1,-1):
#     avg = total/(N-i-1)
#     if not(center[i] - L < avg < center[i] + L):
#         print('unstable')
#         break
#     total += center[i]
# else:
#     print('stable')

# answer 사용 - 시간 더 걸림
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# total = center[-1]
# answer = 'stable'
# for i in range(N-2,-1,-1):
#     avg = total/(N-i-1)
#     if not(center[i] - L < avg < center[i] + L):
#         answer = 'unstable'
#         break
#     total += center[i]
# print(answer)


# 함수 사용
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# def stable_or_not():
#     total = center[-1]
#     for i in range(N-2,-1,-1):
#         if not(center[i] - L < total/(N-i-1) < center[i] + L):
#             return 'unstable'
#         total += center[i]
#     return 'stable'
# print(stable_or_not())


# abs 사용
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# def stable_or_not():
#     total = center[-1]
#     for i in range(N-2,-1,-1):
#         if not(abs(total/(N-i-1) - center[i]) < L):
#             return 'unstable'
#         total += center[i]
#     return 'stable'
# print(stable_or_not())

# abs x - abs 쓴 것보다 시간 더 나옴
# N, L = map(int, input().split())
# center = list(map(int, input().split()))
# def stable_or_not():
#     total = center[-1]
#     for i in range(N-2,-1,-1):
#         if not(-L < total/(N-i-1) - center[i] < L):
#             return 'unstable'
#         total += center[i]
#     return 'stable'
# print(stable_or_not())