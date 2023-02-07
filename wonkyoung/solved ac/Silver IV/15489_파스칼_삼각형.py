#230207
# R, C, W = map(int, input().split())
# triangle = [[1], [1, 1]]
# length, total = 2, 0
# cnt = 1
# for i in range(1, R+W):
#     if length <= i:
#         row = [1] * i
#         for j in range(1, i-1):
#             row[j] = sum(triangle[-1][j-1:j+1])
#         triangle.append(row)
#         length += 1
#     if R <= i:
#         for dc in range(cnt):
#             total += triangle[i][C+dc-1]
#         cnt += 1
# print(total)


#
# def find_total():
#     triangle = [[1], [1, 1]]
#     length, total, cnt = 2, 0, 1
#     for i in range(1, R+W):
#         if length <= i:
#             row = [1] * i
#             for j in range(1, i-1):
#                 row[j] = sum(triangle[-1][j-1:j+1])
#             triangle.append(row)
#             length += 1
#         if R <= i:
#             for dc in range(cnt):
#                 total += triangle[i][C+dc-1]
#             cnt += 1
#     return total
#
# R, C, W = map(int, input().split())
# print(find_total())


# sum
def find_total():
    triangle = [[1], [1, 1]]
    length, total, cnt = 2, 0, 1
    for i in range(1, R+W):
        if length <= i:
            row = [1] * i
            for j in range(1, i-1):
                row[j] = sum(triangle[-1][j-1:j+1])
            triangle.append(row)
            length += 1
        if R <= i:
            total += sum(triangle[i][C-1:C+cnt-1])
            cnt += 1
    return total

R, C, W = map(int, input().split())
print(find_total())
