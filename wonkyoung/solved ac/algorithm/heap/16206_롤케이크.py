#221019
# 틀림
# from heapq import heappush, heappop
# N, M = map(int, input().split())
# rollcakes = list(map(int, input().split()))
# cut_cnt = []
# cnt = 0
# for rollcake in rollcakes:
#     if rollcake > 10:
#         heappush(cut_cnt, (rollcake%10, rollcake//10))
#     elif rollcake == 10:
#         cnt += 1
#
# for _ in range(len(cut_cnt)):
#     remain, new_cnt = heappop(cut_cnt)
#     if M == 0 and remain > 0:
#         break
#     if remain == 0:
#         new_cnt = min(new_cnt , M + 1)
#         M -= new_cnt - 1
#         cnt += new_cnt
#     else:
#         new_cnt = min(new_cnt , M)
#         M -= new_cnt
#         cnt += new_cnt
# print(cnt)


#221022
# from heapq import heappush, heappop
# N, M = map(int, input().split())
# rollcakes = list(map(int, input().split()))
# cut_cnt = []
# cnt = 0
# for rollcake in rollcakes:
#     if rollcake > 10:
#         heappush(cut_cnt, (rollcake%10, rollcake//10))
#     elif rollcake == 10:
#         cnt += 1
#
# for _ in range(len(cut_cnt)):
#     remain, new_cnt = heappop(cut_cnt)
#     if M <= 0:
#         break
#
#     if remain == 0:
#         # 몫만큼 cnt 증가
#         # 몫-1 만큼 M 감소
#         # M < 몫일 경우에는 M
#         if new_cnt <= M + 1:
#             M -= new_cnt - 1
#         else:
#             new_cnt = M
#             M = 0
#     else:
#         # 몫만큼 cnt 증가
#         # 몫만큼 M 감소
#         # M < 몫일 경우에는 M
#         new_cnt = min(new_cnt, M)
#         M -= new_cnt
#     cnt += new_cnt
# print(cnt)


# 정리
# from heapq import heappush, heappop
# N, M = map(int, input().split())
# rollcakes = list(map(int, input().split()))
# cut_cnt = []
# cnt = 0
# for rollcake in rollcakes:
#     if rollcake > 10:
#         heappush(cut_cnt, (rollcake%10, rollcake//10))
#     elif rollcake == 10:
#         cnt += 1
#
# for _ in range(len(cut_cnt)):
#     remain, new_cnt = heappop(cut_cnt)
#     if M <= 0:
#         break
#     zero = int(remain == 0)
#     if new_cnt <= M + zero:
#         M -= new_cnt - zero
#     else:
#         new_cnt = M
#         M = 0
#     cnt += new_cnt
# print(cnt)


# 함수형
def find_cnt():
    from heapq import heappush, heappop
    N, M = map(int, input().split())
    rollcakes = list(map(int, input().split()))
    cut_cnt = []
    cnt = 0
    for rollcake in rollcakes:
        if rollcake > 10:
            heappush(cut_cnt, (rollcake%10, rollcake//10))
        elif rollcake == 10:
            cnt += 1

    for _ in range(len(cut_cnt)):
        remain, new_cnt = heappop(cut_cnt)
        if M <= 0:
            return cnt
        zero = int(remain == 0)
        if new_cnt <= M + zero:
            M -= new_cnt - zero
        else:
            new_cnt = M
            M = 0
        cnt += new_cnt
    return cnt

print(find_cnt())