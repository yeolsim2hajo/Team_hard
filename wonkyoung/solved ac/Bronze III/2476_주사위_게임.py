#220929
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# max_val = 0
# for _ in range(N):
#     dice = {i:0 for i in range(1,7)}
#     cases = map(int, new_input().split())
#     for i in cases:
#         dice[i] += 1
#     for i in range(1, 7):
#         if dice[i] == 3:
#             max_val = max(max_val, 10000 + i * 1000)
#             break
#         elif dice[i] == 2:
#             max_val = max(max_val, 1000 + i * 100)
#             break
#         else:
#             max_val = max(max_val, i * 100)
# print(max_val)

# 함수화
def main():
    import sys
    new_input = sys.stdin.readline
    N = int(new_input())
    max_val = 0

    def calc():
        nonlocal max_val
        for i in range(6, 0, -1):
            if dice[i] == 3:
                max_val = max(max_val, 10000 + i * 1000)
                return
            elif dice[i] == 2:
                max_val = max(max_val, 1000 + i * 100)
                return
            else:
                max_val = max(max_val, i * 100)

    for _ in range(N):
        dice = {i:0 for i in range(1,7)}
        cases = map(int, new_input().split())
        for i in cases:
            dice[i] += 1
        calc()

    print(max_val)

main()

