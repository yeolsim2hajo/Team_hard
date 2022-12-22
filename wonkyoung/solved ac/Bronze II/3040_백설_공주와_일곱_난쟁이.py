#221222
# numbers = [int(input()) for _ in range(9)]
# path, answer = [], []
# finished = False
# def dfs(level=0, start=0, total=0):
#     global finished, answer
#     if finished or total > 100:
#         return
#     if level == 7:
#         if total == 100:
#             finished = True
#             answer = list(map(str, path))
#         return
#     for i in range(start, 9):
#         path.append(numbers[i])
#         dfs(level+1, i+1, total+numbers[i])
#         path.pop()
#
# dfs()
# print('\n'.join(answer))


# print
# numbers = [int(input()) for _ in range(9)]
# path, answer = [], []
# finished = False
# def dfs(level=0, start=0, total=0):
#     global finished, answer
#     if finished or total > 100:
#         return
#     if level == 7:
#         if total == 100:
#             finished = True
#             answer = path[:]
#         return
#     for i in range(start, 9):
#         path.append(numbers[i])
#         dfs(level+1, i+1, total+numbers[i])
#         path.pop()
#
# dfs()
# print(*answer, sep='\n')


# main
# def find_answer():
#     numbers = [int(input()) for _ in range(9)]
#     path, answer = [], []
#     finished = False
#     def dfs(level=0, start=0, total=0):
#         nonlocal finished, answer
#         if finished or total > 100:
#             return
#         if level == 7:
#             if total == 100:
#                 finished = True
#                 answer = list(map(str, path))
#             return
#         for i in range(start, 9):
#             path.append(numbers[i])
#             dfs(level+1, i+1, total+numbers[i])
#             path.pop()
#
#     dfs()
#     return '\n'.join(answer)
# print(find_answer())