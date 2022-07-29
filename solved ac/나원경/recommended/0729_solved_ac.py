#15655 N과 M
# N, M = map(int, input().split())
# arr = sorted(map(int, input().split()))
# def dfs(arg, start):
#     if arg == M:
#         print(*path)
#         return
#     for j in range(start, N):
#         path.append(arr[j])
#         dfs(arg+1, j+1)
#         path.pop()
#
# for i in range(N-M+1):
#     path = [arr[i]]
#     dfs(1,i+1)

# 시간 더 걸림
def find_answer():
    N, M = map(int, input().split())
    arr = sorted(map(int, input().split()))

    def dfs(arg, start):
        if arg == M:
            print(*path)
            return
        for j in range(start, N):
            path.append(arr[j])
            dfs(arg + 1, j + 1)
            path.pop()

    for i in range(N - M + 1):
        path = [arr[i]]
        dfs(1, i + 1)
find_answer()