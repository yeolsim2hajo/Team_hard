# https://www.acmicpc.net/problem/1992
# 230310
# N = int(input())
# video = [input() for _ in range(N)]
# direct = [(0, 0), (0, 1), (1, 0), (1, 1)]
# def div_conq(length, index):
#     if length == 1:
#         # quot = index//4
#         # row = col = quot * 2
#         # for j in range(4):
#         #     row = quot * 2 + direct[j][0]
#         #     col = quot * 2 + direct[j][1]
#         #     print(row, col)
#         return index
#         # return video[row][col]
#     # print(length, index)
#     results = [[] for _ in range(length)]
#     half = length//2
#     square = length * length
#     half_square = square//4
#     # same = True
#     for i in range(4):
#         new_index = index + half_square * i
#         result = div_conq(half, new_index)
#         new_index%square
#         print(result)
#         # print(length, square*index+i)
#         # if same and i:
#         #     if results[i][0] != result:
#         #         results[i].extend([results[i][0]]*(i-1))
#         #         results[i].append(result)
#         #         same = False
#         # else:
#         #     results[i].append(result)
# print(div_conq(N, 0))

# 230312
# N = int(input())
# video = [input() for _ in range(N)]
# direct = [(0, 0), (0, 1), (1, 0), (1, 1)]
# def div_conq(length, index):
#     if length == 1:
#         return index
#     # print(length, index)
#     results = []
#     half = length//2
#     square = length * length
#     half_square = square//4
#     # same = True
#     for i in range(4):
#         new_index = index + half_square * i
#         result = div_conq(half, new_index)
#         results.append((new_index%square, result))
#         print(new_index%square, result)
#         # print(result)
#         # print(length, square*index+i)
#         # if same and i:
#         #     if results[i][0] != result:
#         #         results[i].extend([results[i][0]]*(i-1))
#         #         results[i].append(result)
#         #         same = False
#         # else:
#         #     results[i].append(result)
#     return index
# print(div_conq(N, 0))


#230316
# 참고
# def stretch_video(length, y, x):
#     if length == 2:
#         for dy, dx in direct:
#             ny, nx = y+dy, x+dx
#             print(ny, nx)
#         return
#     half = length//2
#     for dy, dx in direct:
#         ny, nx = y + dy*half, x + dx*half
#         stretch_video(half, ny, nx)
#
# stretch_video(4, 0, 0)

# 분할 정복 + list
# N = int(input())
# video = [input() for _ in range(N)]
# direct = [(0, 0), (0, 1), (1, 0), (1, 1)]
#
# def div_conq(length, y, x):
#     results = []
#     half = length//2
#     same = True
#     before = '-1'
#     for dy, dx in direct:
#         ny, nx = y + dy*half, x + dx*half
#         if length > 2:
#             result = div_conq(half, ny, nx)
#         else:
#             result = video[ny][nx]
#         if same:
#             if before != '-1':
#                 if before != result or len(before) > 1:
#                     same = False
#             before = result
#         results.append(result)
#     if same:
#         return result
#     str_results = ''.join(results)
#     return f'({str_results})'
#
# if N == 1:
#     print(video[0])
# else:
#     str_compact = div_conq(N, 0, 0)
#     print(str_compact)


#
# N = int(input())
# video = [input() for _ in range(N)]
# direct = [(0, 0), (0, 1), (1, 0), (1, 1)]
#
# def div_conq(length, y, x):
#     results = ''
#     half = length//2
#     same = True
#     before = '-1'
#     for dy, dx in direct:
#         ny, nx = y + dy*half, x + dx*half
#         if length > 2:
#             result = div_conq(half, ny, nx)
#         else:
#             result = video[ny][nx]
#         if same:
#             if before != '-1':
#                 if before != result or len(before) > 1:
#                     same = False
#             before = result
#         results += result
#     if same:
#         return result
#     return f'({results})'
#
# if N == 1:
#     print(video[0])
# else:
#     str_compact = div_conq(N, 0, 0)
#     print(str_compact)


#
def compress():
    N = int(input())
    video = [input() for _ in range(N)]
    if N == 1:
        return video[0]

    direct = [(0, 0), (0, 1), (1, 0), (1, 1)]
    def div_conq(length, y, x):
        results = ''
        half = length//2
        same = True
        before = '-1'
        for dy, dx in direct:
            ny, nx = y + dy*half, x + dx*half
            if length > 2:
                result = div_conq(half, ny, nx)
            else:
                result = video[ny][nx]
            if same:
                if before != '-1':
                    if before != result or len(before) > 1:
                        same = False
                before = result
            results += result
        if same:
            return result
        return f'({results})'

    return div_conq(N, 0, 0)
print(compress())

