#19583 싸이버 개강 총회
# import sys
# new_input = sys.stdin.readline
# time_list = new_input().split()
# for i in range(3):
#     time_list[i] = time_list[i].split(':')
#     time_list[i] = int(time_list[i][0]) * 60 + int(time_list[i][1])
# check_in, check_out = set(), set()
# while True:
#     try:
#         chat_time, name = new_input().split()
#         hour, minute = chat_time.split(':')
#         total = int(hour) * 60 + int(minute)
#         if total <= time_list[0]:
#             check_in.add(name)
#         elif time_list[1] <= total <= time_list[2]:
#             check_out.add(name)
#     except:
#         break
# print(len(check_in & check_out))


# 시간 덜 걸림
# import sys
# new_input = sys.stdin.readline
# time_list = new_input().split()
# for i in range(3):
#     time_list[i] = time_list[i].split(':')
#     time_list[i] = time_list[i][0] + time_list[i][1]
# check_in, check_out = set(), set()
# while True:
#     try:
#         chat_time, name = new_input().split()
#         hour, minute = chat_time.split(':')
#         total = hour+minute
#         if total <= time_list[0]:
#             check_in.add(name)
#         elif time_list[1] <= total <= time_list[2]:
#             check_out.add(name)
#     except:
#         break
# print(len(check_in & check_out))


# 시간 더 줄어듦
# import sys
# new_input = sys.stdin.readline
# time_list = new_input().split()
# check_in, check_out = set(), set()
# while True:
#     try:
#         chat_time, name = new_input().split()
#         if chat_time <= time_list[0]:
#             check_in.add(name)
#         elif time_list[1] <= chat_time <= time_list[2]:
#             check_out.add(name)
#     except:
#         break
# print(len(check_in & check_out))



# 시간 더 걸림
# import sys
# new_input = sys.stdin.readline
# time_list = new_input().split()
# check_in, check_out = set(), set()
# while True:
#     chat = new_input().split()
#     if not chat:
#         break
#     if chat[0] <= time_list[0]:
#         check_in.add(chat[1])
#     elif time_list[1] <= chat[0] <= time_list[2]:
#         check_out.add(chat[1])
# print(len(check_in & check_out))


# 함수로
# import sys
# new_input = sys.stdin.readline
# time_list = new_input().split()
# def check():
#     check_in, check_out = set(), set()
#     while True:
#         chat = new_input().split()
#         if not chat:
#             return len(check_in & check_out)
#         if chat[0] <= time_list[0]:
#             check_in.add(chat[1])
#         elif time_list[1] <= chat[0] <= time_list[2]:
#             check_out.add(chat[1])
# print(check())

# 함수로2
# import sys
# new_input = sys.stdin.readline
# time_list = new_input().split()
# def check():
#     check_in, check_out = set(), set()
#     while True:
#         try:
#             chat_time, name = new_input().split()
#             if chat_time <= time_list[0]:
#                 check_in.add(name)
#             elif time_list[1] <= chat_time <= time_list[2]:
#                 check_out.add(name)
#         except:
#             return len(check_in & check_out)
# print(check())


# 전체를 함수로
def check():
    import sys
    new_input = sys.stdin.readline
    time_list = new_input().split()
    check_in, check_out = set(), set()
    while True:
        try:
            chat_time, name = new_input().split()
            if chat_time <= time_list[0]:
                check_in.add(name)
            elif time_list[1] <= chat_time <= time_list[2]:
                check_out.add(name)
        except:
            return len(check_in & check_out)
print(check())