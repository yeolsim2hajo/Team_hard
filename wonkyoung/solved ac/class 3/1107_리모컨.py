#230117
# bfs
from collections import deque
N = input()
M = int(input())
able_buttons = set(map(str,range(10)))
to_str, to_int = list(able_buttons), {str(i):i for i in range(10)}
int_N = int(N)
min_cnt = abs(int_N-100)
if M:
    able_buttons = able_buttons - set(input().split())
q = deque()
length = len(N)
len_q = 0
def append_num(index, now, new_length):
    global len_q
    if index >= length:
        return
    num = N[index]
    int_num = to_int[num]
    max_limit = 10-int_num if int_num <= 5 else int_num
    # if int_num <= 5:
    #     min_limit, max_limit = int_num+1, 10-int_num
    # else:
    #     min_limit, max_limit = int_num+1, 10-int_num

    if num in able_buttons:
        q.append((index, now+num))
        len_q += 1
    else:
        print(max_limit)
        for i in range(1, max_limit):
            plus, minus = int_num+i, int_num-i
            print(plus, minus)
            if plus < 10 and to_str[plus] in able_buttons:
                # print(1, plus)
                q.append((index, now + to_str[plus]))
                new_length += 1
            if minus >= 0:
                if to_str[minus] in able_buttons:
                    # print(2, minus)
                    q.append((index, now + to_str[minus]))
                    new_length += 1
            else:
                minus += 10
                if to_str[minus] in able_buttons:
                    # print(3, minus)
                    q.append((index, now + to_str[minus]))
                    new_length += 1

            if new_length > len_q:
                len_q = new_length
                return
        # for i in range(min_limit, max_limit):
        #     plus, minus = int_num + i, int_num - i
        #     if plus < 10 and to_str[plus] in able_buttons:
        #         q.append((index, to_str[plus]))
        #     elif minus >= 0 and to_str[minus] in able_buttons:
        #         q.append((index, to_str[minus]))
        #     if new_length > len_q:
        #         len_q = new_length
        #         return
append_num(0, '', 0)
print(q)
while q:
    num_i, str_number = q.popleft()
    # print(num_i, str_number)
    if num_i == length - 1:
        new_cnt = abs(int(str_number) - int_N) + length
        if new_cnt < min_cnt:
            min_cnt = new_cnt
        break
    append_num(num_i+1, str_number, len_q)
print(min_cnt)

# dfs
# N = input()
# M = int(input())
# able_buttons = set(map(str,range(10)))
# int_N = int(N)
# min_cnt = abs(int_N-100)
# if M:
#     able_buttons = able_buttons - set(input().split())
# path = []
# now = ''
# for num in N:
#     if num in able_buttons:
#
#     else:





