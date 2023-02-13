#230213
# while True:
#     try:
#         N, M = map(int, input().split())
#         cnt = 0
#         for i in range(N, M+1):
#             check = {str(i): False for i in range(10)}
#             str_i = str(i)
#             for num in str_i:
#                 if check[num]:
#                     break
#                 else:
#                     check[num] = True
#             else:
#                 cnt += 1
#         print(cnt)
#     except EOFError:
#         break


#
# while True:
#     try:
#         N, M = map(int, input().split())
#         cnt = 0
#         for i in range(N, M+1):
#             str_i = str(i)
#             set_i = set(map(str, str_i))
#             if len(str_i) == len(set_i):
#                 cnt += 1
#         print(cnt)
#     except EOFError:
#         break


#
# while True:
#     try:
#         N, M = map(int, input().split())
#         cnt = length = 0
#         for i in range(N, M+1):
#             check = {i: False for i in range(10)}
#             temp_i = i
#             while temp_i:
#                 temp_i, remain = divmod(temp_i, 10)
#                 if check[remain]:
#                     break
#                 else:
#                     check[remain] = True
#             else:
#                 cnt += 1
#         print(cnt)
#     except EOFError:
#         break


#
# import sys
# new_input = sys.stdin.readline
# while True:
#     try:
#         N, M = map(int, new_input().rstrip().split())
#         cnt = 0
#         for i in range(N, M+1):
#             str_i = str(i)
#             set_i = set(map(str, str_i))
#             if len(str_i) == len(set_i):
#                 cnt += 1
#         print(cnt)
#     except Exception:
#         break


#
# import sys
# new_input = sys.stdin.readline
# def find_cnt():
#     N, M = map(int, new_input().rstrip().split())
#     cnt = 0
#     for i in range(N, M + 1):
#         str_i = str(i)
#         set_i = set(map(str, str_i))
#         if len(str_i) == len(set_i):
#             cnt += 1
#     return cnt
#
# while True:
#     try:
#         print(find_cnt())
#     except Exception:
#         break


#
# def find_cnt():
#     import sys
#     new_input = sys.stdin.readline
#     while True:
#         input_value = new_input().rstrip()
#         if input_value:
#             N, M = map(int, input_value.split())
#             cnt = 0
#             for i in range(N, M + 1):
#                 str_i = str(i)
#                 set_i = set(map(str, str_i))
#                 if len(str_i) == len(set_i):
#                     cnt += 1
#             print(cnt)
#         else:
#             break
# find_cnt()


#
# def find_cnt():
#     import sys
#     new_input = sys.stdin.readline
#     while True:
#         input_value = new_input().rstrip()
#         if input_value:
#             N, M = map(int, input_value.split())
#             cnt = length = 0
#             temp_n = N
#             while temp_n:
#                 temp_n //= 10
#                 length += 1
#             limit = 10 ** (length)
#             for i in range(N, M + 1):
#                 set_i = set(map(str, str(i)))
#                 # print(length, set_i)
#                 if limit == i:
#                     length += 1
#                     limit *= 10
#                 if length == len(set_i):
#                     cnt += 1
#             print(cnt)
#         else:
#             break
# find_cnt()


#
def find_cnt():
    import sys
    new_input = sys.stdin.readline
    while True:
        input_value = new_input().rstrip()
        if input_value:
            N, M = map(int, input_value.split())
            cnt = length = 0
            temp_n = N
            while temp_n:
                temp_n //= 10
                length += 1
            limit = 10 ** (length)
            for i in range(N, M + 1):
                set_i = set(map(str, str(i)))
                # print(length, set_i)
                if limit == i:
                    length += 1
                    limit *= 10
                if length == len(set_i):
                    cnt += 1
            print(cnt)
        else:
            break
find_cnt()