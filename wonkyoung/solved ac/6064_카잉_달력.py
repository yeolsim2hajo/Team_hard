#221123
# import sys
# new_input = sys.stdin.readline
# def find_answer():
#     M, N, x, y = map(int, new_input().split())
#     if x == y:
#         return x
#     for i in range(0, N+1):
#         assumption = M * i + x
#         if (assumption - 1) % N + 1 == y:
#             return assumption
#     return -1
# T = int(new_input())
# for _ in range(T):
#     print(find_answer())


# if문 제거 => 더 걸림
# import sys
# new_input = sys.stdin.readline

# def find_answer():
#     M, N, x, y = map(int, new_input().split())
#     for i in range(0, N+1):
#         assumption = M * i + x
#         if (assumption - 1) % N + 1 == y:
#             return assumption
#     return -1

# T = int(new_input())
# for _ in range(T):
#     print(find_answer())


# 반복 횟수 줄임
# import sys
# new_input = sys.stdin.readline

# def find_answer():
#     M, N, x, y = map(int, new_input().split())
#     # 작은 수를 N에 대입
#     if M < N:
#         M, N = N, M
#         x, y = y, x
#     for i in range(0, N+1):
#         assumption = M * i + x
#         if (assumption - 1) % N + 1 == y:
#             return assumption
#     return -1

# T = int(new_input())
# for _ in range(T):
#     print(find_answer())

# 반복 횟수 줄임 + if
# import sys
# new_input = sys.stdin.readline

# def find_answer():
#     M, N, x, y = map(int, new_input().split())
#     if x == y:
#         return x
#     # 작은 수를 N에 대입
#     if M < N:
#         M, N = N, M
#         x, y = y, x
#     for i in range(1, N+1):
#         assumption = M * i + x
#         if (assumption - 1) % N + 1 == y:
#             return assumption
#     return -1

# T = int(new_input())
# for _ in range(T):
#     print(find_answer())


# 규칙 찾기
# -0 => +10 => -2 => +8 ...