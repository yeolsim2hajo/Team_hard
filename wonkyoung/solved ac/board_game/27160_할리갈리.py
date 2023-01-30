#230130
# from sys import stdin
# new_input = stdin.readline
# card_cnt = {'STRAWBERRY' : 0, 'BANANA' : 0, 'LIME' : 0, 'PLUM' : 0}
# N = int(new_input())
# for _ in range(N):
#     key, value = input().split()
#     card_cnt[key] += int(value)
# values = card_cnt.values()
# for value in values:
#     if value == 5:
#         bell = 'YES'
#         break
# else:
#     bell = 'NO'
# print(bell)


# 함수
def is_ringed():
    from sys import stdin
    new_input = stdin.readline
    card_cnt = {'STRAWBERRY' : 0, 'BANANA' : 0, 'LIME' : 0, 'PLUM' : 0}

    N = int(new_input())
    for _ in range(N):
        key, value = new_input().split()
        card_cnt[key] += int(value)

    values = card_cnt.values()
    for value in values:
        if value == 5:
            return 'YES'
    return 'NO'

print(is_ringed())


