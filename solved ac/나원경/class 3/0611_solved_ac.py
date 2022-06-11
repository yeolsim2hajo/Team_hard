#5430 AC
# 기본 - 오래 걸림
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# for _ in range(N):
#     commands = new_input().rstrip()
#     N = int(new_input())
#     arr = new_input().strip('[]\n').split(',')
#     rev = False
#     length = N
#     for command in commands:
#         if command == 'R':
#             rev = not rev
#         elif length:
#             if rev:
#                 arr.pop()
#                 length -= 1
#             else:
#                 arr.pop(0)
#                 length -= 1
#         else:
#             print('error')
#             break
#     else:
#         if rev:
#             arr.reverse()
#         print('[',end='')
#         for i in range(length):
#             print(arr[i],end='')
#             if i != length-1:
#                 print(',',end='')
#         print(']')


# deque 사용 & sep, end 사용 - 확실히 빨라짐 (deque 사용이 결정적이지만 sep, end도 꽤 효과 있음)
# import sys
# from collections import deque
# N = int(input())
# new_input = sys.stdin.readline
# for _ in range(N):
#     commands = new_input().rstrip()
#     N = int(new_input())
#     arr = deque()
#     arr.extend(new_input().strip('[]\n').split(','))
#     rev = False
#     length = N
#     for command in commands:
#         if command == 'R':
#             rev = not rev
#         elif length:
#             if rev:
#                 arr.pop()
#                 length -= 1
#             else:
#                 arr.popleft()
#                 length -= 1
#         else:
#             print('error')
#             break
#     else:
#         if rev:
#             arr.reverse()
#         print('[',end='')
#         print(*arr,sep=',',end=']\n')


# 한꺼번에 제거 - 메모리 꽤 차지, 시간은 많이 안 걸림
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# for _ in range(N):
#     commands = new_input().rstrip()
#     N = int(new_input())
#     arr = new_input().strip('[]\n').split(',')
#     front = -1
#     back = length= N
#     rev = False
#     for command in commands:
#         if command == 'R':
#             rev = not rev
#         elif length:
#             if rev:
#                 back -= 1
#             else:
#                 front += 1
#             length -= 1
#         else:
#             print('error')
#             break
#     else:
#         if length == 0: print([])
#         else:
#             if rev:
#                 if front == -1: front = None
#                 arr = arr[back - 1:front:-1]
#             else:
#                 arr = arr[front+1:back]
#             print('[',end='')
#             print(*arr,sep=',',end=']\n')



#5525 IOIOI - 제약 조건 있을 때만
# N = int(input())
# M = int(input())
# S = input()
# target = 'I'
# for i in range(1,N+1):
#     target += 'OI'
# cnt = idx = 0
# for i in range(M-2*N):
#     if S[i] == 'I':
#         if S[i:i+2*N+1] == target:
#             cnt += 1
# print(cnt)


# 100점
# N = int(input())
# M = int(input())
# S = input()
# target = 'I'
# for i in range(1,N+1):
#     target += 'OI'
# cnt = idx = seq = 0
# while idx+2*N < M:
#     if seq:
#         for _ in range(N):
#             if S[idx+2*N+1:idx+2*N+3] == 'OI':
#                 idx += 2
#                 cnt += 1
#             else:
#                 seq = 0
#                 idx += 1
#                 break
#     else:
#         while idx+2*N < M:
#             if S[idx] == 'I' and S[idx:idx+2*N+1] == target:
#                 cnt += 1
#                 seq = 1
#                 break
#             idx += 1
#         else:
#             break
# print(cnt)