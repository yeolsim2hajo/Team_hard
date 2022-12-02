#221202
# horizontal = []
# length = []
# for _ in range(5):
#     horizontal.append(input())
#     length.append(len(horizontal[-1]))
# result = ''
# max_val = max(length)
# for j in range(max_val):
#     for i in range(5):
#         try:
#             result += horizontal[i][j]
#         except:
#             pass
# print(result)


# if 사용
# horizontal = []
# length = []
# for _ in range(5):
#     horizontal.append(input())
#     length.append(len(horizontal[-1]))
# result = ''
# max_val = max(length)
# for j in range(max_val):
#     for i in range(5):
#         if length[i] > j:
#             result += horizontal[i][j]
# print(result)


# length 없애고 try except
# horizontal = []
# max_val = 0
# for _ in range(5):
#     horizontal.append(input())
#     max_val = max(max_val, len(horizontal[-1]))
# result = ''
# for j in range(max_val):
#     for i in range(5):
#         try:
#             result += horizontal[i][j]
#         except:
#             pass
# print(result)


def read_vertical():
    horizontal = []
    length = []
    for _ in range(5):
        horizontal.append(input())
        length.append(len(horizontal[-1]))
    result = ''
    max_val = max(length)
    for j in range(max_val):
        for i in range(5):
            try:
                result += horizontal[i][j]
            except:
                pass
    return result
print(read_vertical())