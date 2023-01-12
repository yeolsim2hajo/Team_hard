# #221112
# def main():
#     import sys
#
#     new_input = sys.stdin.readline
#     N, C = map(int, new_input().split())
#     houses = sorted([int(new_input()) for _ in range(N)])
#     min_num, max_num = houses[0], houses[-1]
#     result = max_num - min_num
#     if C == 2:
#         return result
#     max_width = (result - 1)//(C-1) + 1
#     start, end = 0, max_width
#     while start <= end:
#         mid = (start + end)//2
#         cnt = 0
#         for i in range(N-1):
#             start_index, end_index = 0, N - 1
#             initial = houses[0]
#             while start_index <= end_index:
#                 mid_index = (start_index + end_index) // 2
#                 if initial + mid > houses[mid_index]:
#                     start_index = mid_index + 1

#221113
def main():
    import sys

    new_input = sys.stdin.readline
    N, C = map(int, new_input().split())
    houses = sorted([int(new_input()) for _ in range(N)])
    between_houses = [0]+[houses[i] - houses[i+1] for i in range(N-1)]
    max_num, min_num = houses[-1], houses[0]
    result = max_num - min_num
    if C == 2:
        return result
    max_gap, min_gap = result//(N-1), min(between_houses)
    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2

    # 기준 gap을 결정한다 => 그 gap보다 작으면 cnt += 1 => cnt와 C 비교


