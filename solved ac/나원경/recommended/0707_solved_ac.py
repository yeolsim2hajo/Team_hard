#1244 스위치 켜고 끄기
# N = int(input())
# switch = list(map(int, input().split()))
# M = int(input())
#
# def convert():
#     global switch
#     switch[number-1] = 1 - switch[number-1]
#     if student == 2:
#         left = number-2
#         right = number
#         while left >= 0 and right < N:
#             if switch[left] != switch[right]:
#                 return
#             switch[left] = switch[right] = 1 - switch[left]
#             left -= 1
#             right += 1
#     else:
#         idx = number * 2 - 1
#         while True:
#             if idx > N-1:
#                 return
#             switch[idx] = 1 - switch[idx]
#             idx += number
#
# for _ in range(M):
#     student, number = map(int, input().split())
#     convert()
# for i in range(0,N,20):
#     print(*switch[i:i+20])


# int로 안 바꾸고 - 똑같음
# N = int(input())
# switch = input().split()
# M = int(input())
#
# def convert():
#     global switch
#     on_off = {'0':'1', '1':'0'}
#     switch[number-1] = on_off[switch[number-1]]
#     if student == 2:
#         left = number-2
#         right = number
#         while left >= 0 and right < N:
#             if switch[left] != switch[right]:
#                 return
#             switch[left] = switch[right] = on_off[switch[left]]
#             left -= 1
#             right += 1
#     else:
#         idx = number * 2 - 1
#         while True:
#             if idx > N-1:
#                 return
#             switch[idx] = on_off[switch[idx]]
#             idx += number
#
# for _ in range(M):
#     student, number = map(int, input().split())
#     convert()
# for i in range(0,N,20):
#     print(*switch[i:i+20])

# sys.stdin.readline - for문에서만 사용하기
# import sys
#
# new_input = sys.stdin.readline
# N = int(input())
# switch = input().split()
# M = int(input())
#
# def convert():
#     global switch
#     on_off = {'0':'1', '1':'0'}
#     switch[number-1] = on_off[switch[number-1]]
#     if student == 2:
#         left = number-2
#         right = number
#         while left >= 0 and right < N:
#             if switch[left] != switch[right]:
#                 return
#             switch[left] = switch[right] = on_off[switch[left]]
#             left -= 1
#             right += 1
#     else:
#         idx = number * 2 - 1
#         while True:
#             if idx > N-1:
#                 return
#             switch[idx] = on_off[switch[idx]]
#             idx += number
#
# for _ in range(M):
#     student, number = map(int, new_input().split())
#     convert()
# for i in range(0,N,20):
#     print(*switch[i:i+20])