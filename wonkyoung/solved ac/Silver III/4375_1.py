#230323
# from sys import stdin
# new_input = stdin.readline
# while True:
#     num = new_input().rstrip()
#     if not num:
#         break
#     num = int(num)
#     one_num = 1
#     cnt = 1
#     while one_num%num:
#         cnt += 1
#         one_num = one_num*10 + 1
#     print(cnt)


#
# from sys import stdin
# new_input = stdin.readline
# while True:
#     try:
#         num = int(new_input().rstrip())
#         one_num = cnt = 1
#         while one_num%num:
#             cnt += 1
#             one_num = one_num*10 + 1
#         print(cnt)
#     except:
#         break


#
# from sys import stdin
# new_input = stdin.readline
# while True:
#     num = new_input().rstrip()
#     if num:
#         cnt = len(num)
#         num = int(num)
#         one_num = int('1' * cnt)
#         while one_num%num:
#             cnt += 1
#             one_num = one_num*10 + 1
#         print(cnt)
#     else:
#         break


#
# def find_cnt():
#     from sys import stdin
#     new_input = stdin.readline
#     while True:
#         num = new_input().rstrip()
#         if not num:
#             break
#         num = int(num)
#         one_num = 1
#         cnt = 1
#         while one_num%num:
#             cnt += 1
#             one_num = one_num*10 + 1
#         print(cnt)
# find_cnt()


#
def find_cnt():
    while True:
        try:
            num = int(input())
            one_num = cnt = 1
            while one_num%num:
                cnt += 1
                one_num = one_num*10 + 1
            print(cnt)
        except EOFError:
            return
find_cnt()