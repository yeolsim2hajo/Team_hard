#221208
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     initial = input()
#     target = input()
#     b_to_w = w_to_b = 0
#     for i in range(N):
#         if initial[i] == 'B' and target[i] == 'W':
#             b_to_w += 1
#         elif initial[i] == 'W' and target[i] == 'B':
#             w_to_b += 1
#     print(max(b_to_w, w_to_b))



# sys.stdin.readline
# import sys
#
# new_input = sys.stdin.readline
# T = int(new_input())
# for _ in range(T):
#     N = int(new_input())
#     initial = new_input()
#     target = new_input()
#     b_to_w = w_to_b = 0
#     for i in range(N):
#         if initial[i] == 'B' and target[i] == 'W':
#             b_to_w += 1
#         elif initial[i] == 'W' and target[i] == 'B':
#             w_to_b += 1
#     print(max(b_to_w, w_to_b))


# 함수형
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     T = int(new_input())
#     for _ in range(T):
#         N = int(new_input())
#         initial = new_input()
#         target = new_input()
#         def find_cnt():
#             b_to_w = w_to_b = 0
#             for i in range(N):
#                 if initial[i] == 'B' and target[i] == 'W':
#                     b_to_w += 1
#                 elif initial[i] == 'W' and target[i] == 'B':
#                     w_to_b += 1
#             return max(b_to_w, w_to_b)
#         print(find_cnt())
# find_answer()


# for문 위로 빼기
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     T = int(new_input())
#     def find_cnt(initial, target):
#         b_to_w = w_to_b = 0
#         for i in range(N):
#             if initial[i] == 'B' and target[i] == 'W':
#                 b_to_w += 1
#             elif initial[i] == 'W' and target[i] == 'B':
#                 w_to_b += 1
#         return max(b_to_w, w_to_b)
#     for _ in range(T):
#         N = int(new_input())
#         initial = new_input()
#         target = new_input()
#         print(find_cnt(initial, target))
# find_answer()


# if문 여러 개
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     T = int(new_input())
#     for _ in range(T):
#         N = int(new_input())
#         initial = new_input()
#         target = new_input()
#         def find_cnt():
#             b_to_w = w_to_b = 0
#             for i in range(N):
#                 if initial[i] != target[i]:
#                     if initial[i] == 'B':
#                         b_to_w += 1
#                     else:
#                         w_to_b += 1
#             return max(b_to_w, w_to_b)
#         print(find_cnt())
# find_answer()


# for문 밖에서 함수 정의 - 왜 시간 더 나오지?
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     T = int(new_input())
#
#     def find_cnt():
#         b_to_w = w_to_b = 0
#         for i in range(N):
#             if initial[i] != target[i]:
#                 if initial[i] == 'B':
#                     b_to_w += 1
#                 else:
#                     w_to_b += 1
#         return max(b_to_w, w_to_b)
#
#     for _ in range(T):
#         N = int(new_input())
#         initial = new_input()
#         target = new_input()
#         print(find_cnt())
#
# find_answer()

# rstrip
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     T = int(new_input())
#     for _ in range(T):
#         N = int(new_input())
#         initial = new_input().rstrip()
#         target = new_input().rstrip()
#         def find_cnt():
#             b_to_w = w_to_b = 0
#             for i in range(N):
#                 if initial[i] != target[i]:
#                     if initial[i] == 'B':
#                         b_to_w += 1
#                     else:
#                         w_to_b += 1
#             return max(b_to_w, w_to_b)
#         print(find_cnt())
# find_answer()


# 입력까지 함수 안으로
def find_answer():
    import sys
    new_input = sys.stdin.readline
    T = int(new_input())

    def find_cnt():
        N = int(new_input())
        initial = new_input().rstrip()
        target = new_input().rstrip()
        b_to_w = w_to_b = 0
        for i in range(N):
            if initial[i] != target[i]:
                if initial[i] == 'B':
                    b_to_w += 1
                else:
                    w_to_b += 1
        return max(b_to_w, w_to_b)

    for _ in range(T):
        print(find_cnt())

find_answer()