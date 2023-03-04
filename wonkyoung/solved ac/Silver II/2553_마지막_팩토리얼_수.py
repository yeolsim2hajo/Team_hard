#230301
# 다시
# def find_last_num(N):
#     from math import factorial
#     remain1 = N%10
#     if remain1 < 5:
#         ref = factorial(N - remain1)
#         while True:
#             remain2 = ref%10
#             if remain2:
#                 break
#             ref //= 10
#         if remain1 in {0, 1}:
#             return remain2
#         elif remain1 == 3:
#             remain1 *= 2
#         return (remain2 * remain1)%10
#     else:
#         ref = factorial(N - remain1 + 5)
#         while True:
#             remain2 = ref%10
#             if remain2:
#                 break
#             ref //= 10
#         if remain1 in {5, 6, 8}:
#             return remain2
#         return (remain2 * remain1)%10
#
# # N = int(input())
# # print(find_last_num(N))
# for N in range(31):
#     print(N, find_last_num(N), sep=' ')


#230302
# 틀림
# def find_last(num):
#     from math import factorial
#     if num <= 1:
#         return 1
#     answer = 2
#     for i in range(3, num+1):
#         answer *= i
#         str_ans = str(answer).rstrip('0')
#         for i in range(len(str_ans)-1, -1, -1):
#             if str_ans[i] == '0':
#                 str_ans = str_ans[i+1:]
#                 break
#         answer = int(str_ans)
#     ref = factorial(num)
#     # print(ref)
#     while True:
#         remain = ref%10
#         if remain:
#             break
#         ref //= 10
#     while True:
#         remain = answer%10
#         if remain:
#             return ref%10 == remain
#             # print(num, ref%10, remain)
#             # break
#             # return remain
#         answer //= 10

# N = int(input())
# print(find_last(N))


#230304
# cnt = 0
# total = 1
# for i in range(1, 101):
#     total *= i
#     if i%10 in {4, 5}:
#         print(i, total)
    # cnt += 1
    # if cnt == 10:
    #     cnt = 0
    #     print()

#
# def find_last(N):
#     if N <= 2:
#         return N
#     match = [{} for _ in range(5)]
#     for i in range(2, 10, 2):
#         for j in range(1, 5):
#             match[j][i] = i * j % 10
#     last_num = 2
#     for i in range(3, N+1):
#         if i % 10 == 0:
#             while i % 10 == 0:
#                 i //= 10
#         if i % 5 == 0:
#             five_cnt = 0
#             while i % 5 == 0:
#                 i //= 5
#                 five_cnt += 1
#             for _ in range(five_cnt):
#                 last_num //= 2
#                 if last_num % 2:
#                     last_num += 5
#             last_num = (last_num * i) % 10
#         else:
#             idx = i%5
#             last_num = match[idx][last_num]
#     return last_num
#
# N = int(input())
# print(find_last(N))


#
# def find_last(N):
#     if N <= 2:
#         return N
#     last_num = 2
#     match = [{} for _ in range(5)]
#     for i in range(2, 10, 2):
#         for j in range(1, 5):
#             match[j][i] = i * j % 10
#     for i in range(3, N+1):
#         if i % 10 == 0:
#             while i % 10 == 0:
#                 i //= 10
#         five_cnt = 0
#         while i % 5 == 0:
#             i //= 5
#             five_cnt += 1
#         for _ in range(five_cnt):
#             last_num //= 2
#             if last_num % 2:
#                 last_num += 5
#         idx = i%5
#         last_num = match[idx][last_num]
#     return last_num
#
# N = int(input())
# print(find_last(N))

#
# def find_last(N):
#     if N <= 2:
#         return N
#     last_num = 2
#     match = [{} for _ in range(5)]
#     for i in range(2, 10, 2):
#         for j in range(1, 5):
#             match[j][i] = i * j % 10
#     for i in range(3, N+1):
#         if i % 10 == 0:
#             while i % 10 == 0:
#                 i //= 10
#         if i % 5 == 0:
#             five_cnt = 0
#             while i % 5 == 0:
#                 i //= 5
#                 five_cnt += 1
#             for _ in range(five_cnt):
#                 last_num //= 2
#                 if last_num % 2:
#                     last_num += 5
#         idx = i%5
#         last_num = match[idx][last_num]
#     return last_num
#
# N = int(input())
# print(find_last(N))

#
# def find_last(N):
#     if N <= 2:
#         return N
#     last_num = 2
#     match = [{} for _ in range(5)]
#     for i in range(2, 10, 2):
#         for j in range(1, 5):
#             match[j][i] = i * j % 10
#     for i in range(3, N+1):
#         if i % 10 == 0:
#             while i % 10 == 0:
#                 i //= 10
#         if i % 5 == 0:
#             five_cnt = 1
#             i //= 5
#             while i % 5 == 0:
#                 i //= 5
#                 five_cnt += 1
#             for _ in range(five_cnt):
#                 last_num //= 2
#                 if last_num % 2:
#                     last_num += 5
#         idx = i%5
#         last_num = match[idx][last_num]
#     return last_num
#
# N = int(input())
# print(find_last(N))

#
def find_last(N):
    if N <= 2:
        return N
    last_num = 2
    match = [{} for _ in range(5)]
    for i in range(2, 10, 2):
        for j in range(1, 5):
            match[j][i] = i * j % 10
    for i in range(3, N+1):
        if i % 10 == 0:
            i //= 10
            while i % 10 == 0:
                i //= 10
        if i % 5 == 0:
            five_cnt = 1
            i //= 5
            while i % 5 == 0:
                i //= 5
                five_cnt += 1
            for _ in range(five_cnt):
                last_num //= 2
                if last_num % 2:
                    last_num += 5
        last_num = match[i%5][last_num]
    return last_num

N = int(input())
print(find_last(N))