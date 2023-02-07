#230208
# def solution(dot):
#     x, y = dot
#     if x > 0:
#         if y > 0:
#             return 1
#         return 4
#     elif y > 0:
#         return 2
#     return 3


#
def solution(dot):
    answer = [[2, 1],[3, 4]]
    x, y = dot
    row = 0 if y > 0 else 1
    col = 1 if x > 0 else 0
    return answer[row][col]