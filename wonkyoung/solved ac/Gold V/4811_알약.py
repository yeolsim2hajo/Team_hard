#230119
# 시간 많이 걸림
# import sys
# new_input = sys.stdin.readline
# def cnt_letter(N):
#     cnt = 0
#     def dfs(level, half, whole):
#         nonlocal cnt
#         if level == 2*N-1:
#             cnt += 1
#             return
#         if half:
#             dfs(level+1, half-1, whole)
#         if whole:
#             dfs(level+1, half+1, whole-1)
#
#     dfs(1, 1, N-1)
#     return cnt
# while True:
#     N = int(new_input())
#     if N == 0:
#         break
#     print(cnt_letter(N))


#230127
import sys
new_input = sys.stdin.readline
memoization = [0] * 31
def cnt_letter(N):
    if memoization[N]:
        return memoization[N]
    cnt = 0
    def find_before(level):
        nonlocal cnt
        if memoization[level-1]:
            return memoization[level-1]
        else:
            cnt = find_before(level-1)


    def dfs(level, half, whole):
        nonlocal cnt
        cnt = find_before(level)

    dfs(N, N-1, N-2)
    return cnt
while True:
    N = int(new_input())
    if N == 0:
        break
    print(cnt_letter(N))

