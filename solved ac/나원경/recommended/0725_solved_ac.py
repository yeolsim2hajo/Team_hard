#17212 달나라 토끼를 위한 구매대금 지불 도우미
# 틀림
# N = int(input())
# kind = [7,5,2,1]
# final_cnt = N
# def pay(coin_list, length):
#     total_cnt1, change1 = divmod(N, coin_list[0])
#     total_cnt2, change2 = total_cnt1 - 1, change1 + coin_list[0]
#     for j in range(1,length):
#         total_cnt1 += change1//coin_list[j]
#         change1 %= coin_list[j]
#         total_cnt2 += change2//coin_list[j]
#         change2 %= coin_list[j]
#         if change1 == change2 == 0:
#             return min(total_cnt1, total_cnt2)
#     return min(total_cnt1, total_cnt2)
# if N:
#     for i in range(3):
#         final_cnt = min(final_cnt, pay(kind[i:], 4-i))
# print(final_cnt)

# 틀림
# N = int(input())
# kind = [7,5,2,1]
# final_cnt = N
# def pay(coin_list, length):
#     start = coin_list[0]
#     if N%start == 0:
#         return N//start
#     else:
#         total_cnt1, change1 = divmod(N, start)
#         total_cnt2, change2 = total_cnt1 - 1, change1 + start
#         for j in range(1,length):
#             start = coin_list[j]
#             total_cnt1 += change1//start
#             change1 %= start
#             total_cnt2 += change2//start
#             change2 %= start
#             if change1 == change2 == 0:
#                 return min(total_cnt1, total_cnt2)
#         return min(total_cnt1, total_cnt2)
# if N:
#     for i in range(3):
#         final_cnt = min(final_cnt, pay(kind[i:], 4-i))
# print(final_cnt)


#1193 분수찾기
# X = int(input())
# def find_answer():
#     plus_number = 2
#     start, end, step = 1, plus_number, 1
#     cnt = 0
#     while X > 1:
#         for i in range(start, end, step):
#             cnt += 1
#             if cnt == X:
#                 son = start + i * step
#                 return f'{son}/{plus_number - son}'
#         start, end, step = end, start, -step
#         if end == 1:
#             start += 1
#         else:
#             end += 1
#         plus_number += 1
#     return '1/1'
# print(find_answer())


#2530 인공지능 시계
# A, B, C = map(int, input().split())
# D = int(input())
# total = 3600 * A + 60 * B + C + D
# hour, remain = divmod(total, 3600)
# minute, second = divmod(remain, 60)
# print(hour%24, minute, second)
