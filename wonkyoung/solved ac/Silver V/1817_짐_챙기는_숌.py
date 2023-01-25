#230125
# N, M = map(int, input().split())
# cnt = 0
# if N:
#     book_list = list(map(int, input().split()))
#     now = 0
#     for book in book_list:
#         if now + book <= M:
#             now += book
#         else:
#             cnt += 1
#             now = book
#     cnt += 1
# print(cnt)


# 함수화
# def cnt_box(N, M):
#     if N == 0:
#         return 0
#     book_list = list(map(int, input().split()))
#     cnt, now = 1, 0
#     for book in book_list:
#         if now + book <= M:
#             now += book
#         else:
#             cnt += 1
#             now = book
#     return cnt
#
# N, M = map(int, input().split())
# print(cnt_box(N, M))


# temp 더하고 빼기
# def cnt_box(N, M):
#     if N == 0:
#         return 0
#     book_list = list(map(int, input().split()))
#     cnt, now = 1, 0
#     for book in book_list:
#         temp, now = now, now + book
#         if now > M:
#             cnt += 1
#             now -= temp
#     return cnt
#
# N, M = map(int, input().split())
# print(cnt_box(N, M))

# for문 1에서부터
# def cnt_box(N, M):
#     if N == 0:
#         return 0
#     book_list = list(map(int, input().split()))
#     cnt, now = 1, book_list[0]
#     for i in range(1, N):
#         book = book_list[i]
#         if now + book <= M:
#             now += book
#         else:
#             cnt += 1
#             now = book
#     return cnt
#
# N, M = map(int, input().split())
# print(cnt_box(N, M))


# 공간
def cnt_box(N, M):
    if N == 0:
        return 0
    book_list = list(map(int, input().split()))
    cnt, left = 1, M - book_list[0]
    for book_i in range(1, N):
        book = book_list[book_i]
        if left < book:
            cnt += 1
            left = M - book
        else:
            left -= book
    return cnt

N, M = map(int, input().split())
print(cnt_box(N, M))