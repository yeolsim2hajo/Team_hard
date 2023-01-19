#230119
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))
# number_cnt = [0] * (int(1e4)+1)
# for number in numbers:
#     number_cnt[number] += 1
# numbers = sorted(set(numbers))
# N = len(numbers)
# path = []
# def dfs(level):
#     if level == M:
#         print(*path)
#         return
#     for i in range(N):
#         number = numbers[i]
#         if number_cnt[number]:
#             path.append(numbers[i])
#             number_cnt[number] -= 1
#             dfs(level+1)
#             path.pop()
#             number_cnt[number] += 1
# dfs(0)

#
# def main():
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     number_cnt = [0] * (int(1e4) + 1)
#     for number in numbers:
#         number_cnt[number] += 1
#     numbers = sorted(set(numbers))
#     N = len(numbers)
#     path = []
#
#     def dfs(level):
#         if level == M:
#             print(*path)
#             return
#         for i in range(N):
#             number = numbers[i]
#             if number_cnt[number]:
#                 path.append(numbers[i])
#                 number_cnt[number] -= 1
#                 dfs(level + 1)
#                 path.pop()
#                 number_cnt[number] += 1
#
#     dfs(0)
# main()

#
# def main():
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     number_cnt = [0] * (int(1e4) + 1)
#     contain = set()
#     for number in numbers:
#         number_cnt[number] += 1
#         contain.add(number)
#     contain = sorted(contain)
#     path = []
#
#     def dfs(level):
#         if level == M:
#             print(*path)
#             return
#         for number in contain:
#             if number_cnt[number]:
#                 path.append(number)
#                 number_cnt[number] -= 1
#                 dfs(level + 1)
#                 path.pop()
#                 number_cnt[number] += 1
#
#     dfs(0)
# main()

#
# def main():
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     numbers.sort()
#     number_cnt = [0] * (int(1e4) + 1)
#     contain = []
#     for number in numbers:
#         number_cnt[number] += 1
#         if not contain or contain[-1] != number:
#             contain.append(number)
#     path = []
#
#     def dfs(level):
#         if level == M:
#             print(*path)
#             return
#         for number in contain:
#             if number_cnt[number]:
#                 path.append(number)
#                 number_cnt[number] -= 1
#                 dfs(level + 1)
#                 path.pop()
#                 number_cnt[number] += 1
#
#     dfs(0)
# main()

# dict
def main():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    number_cnt = {}
    for number in numbers:
        if number_cnt.get(number):
            number_cnt[number] += 1
        else:
            number_cnt[number] = 1
    path = []
    keys = sorted(number_cnt.keys())

    def dfs(level):
        if level == M:
            print(*path)
            return
        for number in keys:
            if number_cnt[number]:
                path.append(number)
                number_cnt[number] -= 1
                dfs(level + 1)
                path.pop()
                number_cnt[number] += 1

    dfs(0)
main()