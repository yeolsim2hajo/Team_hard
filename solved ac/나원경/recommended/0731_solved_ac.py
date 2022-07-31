#11441 합 구하기
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# arr = list(map(int, new_input().split()))
# M = int(new_input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     print(sum(arr[start-1:end]))


# 누적합 이용
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# arr = list(map(int, new_input().split()))
# acc = [arr[0]]
# for i in range(1,N):
#     acc.append(acc[-1] + arr[i])
# M = int(new_input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     if start == 1:
#         print(acc[end-1])
#     elif start == end:
#         print(arr[start-1])
#     else:
#         print(acc[end-1] - acc[start-2])

# 시간 더 걸림
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# arr = list(map(int, new_input().split()))
# acc = arr[:]
# for i in range(1,N):
#     acc[i] += acc[i-1]
# M = int(new_input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     if start == 1:
#         print(acc[end-1])
#     elif start == end:
#         print(arr[start-1])
#     else:
#         print(acc[end-1] - acc[start-2])


# 시간 덜 걸림
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# arr = list(map(int, new_input().split()))
# acc = [arr[0]]
# for i in range(1,N):
#     acc.append(acc[-1] + arr[i])
# M = int(new_input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     answer = acc[end-1]
#     if start > 1:
#         answer -= acc[start-2]
#     print(answer)


# 약간 더 걸림
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# arr = list(map(int, new_input().split()))
# acc = [arr[0]]
# for i in range(1,N):
#     acc.append(acc[-1] + arr[i])
# M = int(new_input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     minus = acc[start-2]
#     if start == 1:
#         minus = 0
#     print(acc[end-1] - minus)


# 더 걸릴 줄 몰랐음
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# arr = list(map(int, new_input().split()))
# acc = [0, arr[0]]
# for i in range(1,N):
#     acc.append(acc[-1] + arr[i])
# M = int(new_input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     answer = acc[end] - acc[start-1]
#     print(answer)

#input과 섞으면 시간 더 나옴
# import sys
#
# new_input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# acc = [arr[0]]
# for i in range(1,N):
#     acc.append(acc[-1] + arr[i])
# M = int(input())
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     answer = acc[end-1]
#     if start > 1:
#         answer -= acc[start-2]
#     print(answer)


# 리스트에 0 추가 - 시간 덜 걸림
import sys

new_input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
acc = [0, arr[0]]
for i in range(1,N):
    acc.append(acc[-1] + arr[i])
M = int(input())
for _ in range(M):
    start, end = map(int, new_input().split())
    answer = acc[end]
    if start > 1:
        answer -= acc[start-1]
    print(answer)