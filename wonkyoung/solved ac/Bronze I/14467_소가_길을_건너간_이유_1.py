#230129
# N = int(input())
# cow_list = {}
# cnt = 0
# for _ in range(N):
#     cow, position = input().split()
#     if cow_list.get(cow):
#         if cow_list[cow] != position:
#             cnt += 1
#     cow_list[cow] = position
# print(cnt)

# 정리
def cnt_position_change():
    N = int(input())
    cow_list = {}
    cnt = 0
    for _ in range(N):
        cow, position = input().split()
        if cow_list.get(cow):
            if cow_list[cow] != position:
                cnt += 1
        cow_list[cow] = position
    return cnt
print(cnt_position_change())
