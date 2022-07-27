#15728 에리 - 카드
# 틀림
# N, K = map(int, input().split())
# share_cards = sorted(list(map(int, input().split())))
# team_cards = sorted(list(map(int, input().split())))
# def remove_cards(option):
#     if option:
#         for _ in range(K):
#             team_cards.pop()
#     else:
#         start, end = 0, N-1
#         for _ in range(K):
#             start_value, end_value = share_cards[start] * team_cards[start], share_cards[end] * team_cards[end]
#             if start_value > end_value:
#                 team_cards.pop(0)
#             elif start_value < end_value:
#                 team_cards.pop()
#             else:
#                 for i in range(end):
#                     start_value, end_value = share_cards[i] * team_cards[0], share_cards[-i] * team_cards[-1]
#                     if start_value > end_value:
#                         team_cards.pop(0)
#                         break
#                     elif start_value < end_value:
#                         team_cards.pop()
#                         break
#                 team_cards.pop()
#             end -= 1
#
# mid_num = share_cards[N//2]
# if N%2 and mid_num == 0:
#     remove_cards(0)
#     print(max(team_cards[-1] * share_cards[-1], team_cards[0] * share_cards[0]))
# elif mid_num > 0:
#     remove_cards(1)
#     print(team_cards[-1] * share_cards[-1])
# else:
#     team_cards = team_cards[::-1]
#     remove_cards(1)
#     print(team_cards[-1] * share_cards[0])



#1703 생장점
# def main():
#     while True:
#         old, *info = map(int, input().split())
#         if old == 0:
#             return
#         total = info[0] - info[1]
#         for i in range(1,old):
#             total = total*info[2*i] - info[2*i+1]
#         print(total)
# main()

# 시간 더 걸림
# def main():
#     while True:
#         old, *info = map(int, input().split())
#         if old == 0:
#             return
#         total = info[0] - info[1]
#         for i in range(2,2*old,2):
#             total = total*info[i] - info[i+1]
#         print(total)
# main()


# old 쓰든 안 쓰든 똑같
# def main():
#     while True:
#         info = list(map(int, input().split()))
#         if info[0] == 0:
#             return
#         total = info[1] - info[2]
#         for i in range(1, info[0]):
#             total = total*info[2*i+1] - info[2*i+2]
#         print(total)
# main()