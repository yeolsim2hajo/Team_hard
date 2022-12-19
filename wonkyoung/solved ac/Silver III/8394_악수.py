#221219
# N = int(input())
# last_two = [1, 2]
# if N <= 2:
#     print(last_two[N-1])
# else:
#     for i in range(2, N):
#         last_number = (last_two[0] + last_two[1])%10
#         if i%2:
#             last_two[1] = last_number
#         else:
#             last_two[0] = last_number
#     print(last_two[(N-1)%2])


# % 마지막에만 => 시간 초과
# N = int(input())
# last_two = [1, 2]
# if N <= 2:
#     print(last_two[N-1])
# else:
#     for i in range(2, N):
#         last_number = last_two[0] + last_two[1]
#         if i%2:
#             last_two[1] = last_number
#         else:
#             last_two[0] = last_number
#     print(last_two[(N-1)%2]%10)


# if문 제거
# N = int(input())
# last_two = [1, 2]
# if N <= 2:
#     print(last_two[N-1])
# else:
#     for i in range(2, N):
#         last_number = (last_two[0] + last_two[1])%10
#         last_two[i%2] = last_number
#     print(last_two[(N-1)%2])

# deque 사용 - 더 걸림
# from collections import deque
# N = int(input())
# last_two = deque([1, 2])
# if N <= 2:
#     print(last_two[N-1])
# else:
#     for i in range(2, N):
#         last_number = (last_two[0] + last_two[1])%10
#         last_two.popleft()
#         last_two.append(last_number)
#     print(last_two[-1])


# sliding window + deque
# from collections import deque
# N = int(input())
# last_two = deque([1, 2])
# total = 3
# if N <= 2:
#     print(last_two[N-1])
# else:
#     for i in range(2, N):
#         last_two.append(total)
#         total += total
#         total -= last_two.popleft()
#     print(last_two[-1])