#51 merge sort
def merge_sort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    mid = length//2
    one = merge_sort(lst[:mid])
    two = merge_sort(lst[mid:])
    result = []

    while one and two:
        if one[0] < two[0]:
            result.append(one.pop(0))
        else:
            result.append(two.pop(0))
    while one:
        result.append(one.pop())
    while two:
        result.append(two.pop())
    return result

input_lst = [180,145,165,45,170,175,173,171]
print(merge_sort(input_lst))


#70 행렬 곱하기 - 다시
# a = ([1,2],[2,4])
# b = ([1,0],[0,3])
# a_n = len(a)
# a_m = len(a[0])
# b_n = len(b)
# b_m = len(b[0])
# if a_n == b_m and a_m == b_n:
#     result = [[] for _ in range(a_n)]
#     for i in range(a_n):
#         total = 0
#         for j in range(a_m):
#             for k in range(b_m):
#                 total+=a[i][k]*b[j][k]
#
#         result[i].append(a[i][j]*b[j][i])
#     print(tuple(result))
# else:
#     print(-1)