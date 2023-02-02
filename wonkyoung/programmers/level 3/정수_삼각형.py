#230202
# 시간 초과
# def solution(triangle):
#     n = len(triangle)
#     answer = [[]]
#     answer[0].extend(triangle[0])
#     for i in range(1, n):
#         temp = [[] for i in range(i + 1)]
#         for j in range(i):
#             for k in answer[j]:
#                 for dj in range(2):
#                     temp[j + dj].append(k + triangle[i][j + dj])
#         answer = [num_list[:] for num_list in temp]
#     max_val = 0
#     for num_list in answer:
#         max_num = max(num_list)
#         if max_val < max_num:
#             max_val = max_num
#     return max_val
# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


# 아래에서부터
def solution(triangle):
    n = len(triangle)
    for i in range(n-1, 0, -1):
        bottom = triangle[i]
        for j in range(i):
            triangle[i-1][j] += max(bottom[j], bottom[j+1])
    return triangle[0][0]
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
