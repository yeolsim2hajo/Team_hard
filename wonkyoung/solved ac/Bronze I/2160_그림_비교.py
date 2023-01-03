#230102
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# pictures = [[new_input().rstrip() for _ in range(5)] for _ in range(N)]
# cnt = [[0] * i for i in range(N)]
# for i in range(5):
#     for j in range(7):
#         for k in range(1, N):
#             ref = pictures[k][i][j]
#             for l in range(k):
#                 if ref != pictures[l][i][j]:
#                     cnt[k][l] += 1
# picture_no, min_cnt = '', 36
# for i in range(1, N):
#     for j in range(i):
#         if cnt[i][j] < min_cnt:
#             picture_no = f'{j+1} {i+1}'
#             min_cnt = cnt[i][j]
# print(picture_no)


# 함수형
def conf_picture():
    import sys
    new_input = sys.stdin.readline
    N = int(new_input())
    pictures = [[new_input().rstrip() for _ in range(5)] for _ in range(N)]
    cnt = [[0] * i for i in range(N)]
    def fill_cnt():
        for i in range(5):
            for j in range(7):
                for k in range(1, N):
                    ref = pictures[k][i][j]
                    for l in range(k):
                        if ref != pictures[l][i][j]:
                            cnt[k][l] += 1
    def find_cnt():
        picture_no, min_cnt = '', 36
        for i in range(1, N):
            for j in range(i):
                if cnt[i][j] < min_cnt:
                    picture_no = f'{j+1} {i+1}'
                    min_cnt = cnt[i][j]
        return picture_no

    fill_cnt()
    return find_cnt()
print(conf_picture())

