#221212
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# bulbs = ['']
# bulbs.extend(new_input().split())
#
# def command_action(command, first, second):
#     if command == 1:
#         bulbs[first] = str(second)
#     elif command == 2:
#         for i in range(first, second+1):
#             bulbs[i] = '0' if bulbs[i] == '1' else '1'
#     else:
#         value = str(command - 3)
#         bulbs[first:second+1] = [value] * (second - first + 1)
#
# for _ in range(M):
#     command, first, second = map(int, new_input().split())
#     command_action(command, first, second)
#
# print(' '.join(bulbs[1:]))


# main
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = ['']
#     bulbs.extend(new_input().split())
#
#     def command_action(command, first, second):
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             for i in range(first, second+1):
#                 bulbs[i] = '0' if bulbs[i] == '1' else '1'
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action(command, first, second)
#
#     return ' '.join(bulbs[1:])
#
# print(main())


# extend X
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = [''] + new_input().split()
#
#     def command_action(command, first, second):
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             for i in range(first, second+1):
#                 bulbs[i] = '0' if bulbs[i] == '1' else '1'
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action(command, first, second)
#
#     return ' '.join(bulbs[1:])
#
# print(main())


# switch 함수
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = ['']
#     bulbs.extend(new_input().split())
#
#     def switch(state):
#         match = {'0': '1', '1': '0'}
#         return match[state]
#
#     def command_action(command, first, second):
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             for i in range(first, second+1):
#                 bulbs[i] = switch(bulbs[i])
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action(command, first, second)
#
#     return ' '.join(bulbs[1:])
#
# print(main())



# map + switch
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = ['']
#     bulbs.extend(new_input().split())
#
#     def switch(state):
#         match = {'0': '1', '1': '0'}
#         return match[state]
#
#     def command_action(command, first, second):
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             bulbs[first:second + 1] = list(map(switch, bulbs[first:second + 1]))
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action(command, first, second)
#
#     return ' '.join(bulbs[1:])
#
# print(main())


# match 사용
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = ['']
#     bulbs.extend(new_input().split())
#     match = {'0': '1', '1': '0'}
#
#     def command_action(command, first, second):
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             for i in range(first, second + 1):
#                 bulbs[i] = match[bulbs[i]]
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action(command, first, second)
#
#     return ' '.join(bulbs[1:])
#
# print(main())


# join 밖으로 빼기
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = ['']
#     bulbs.extend(new_input().split())
#     match = {'0': '1', '1': '0'}
#
#     def command_action(command, first, second):
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             for i in range(first, second + 1):
#                 bulbs[i] = match[bulbs[i]]
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action(command, first, second)
#
#     return bulbs[1:]
#
# print(' '.join(main()))


# 인자 X
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     bulbs = ['']
#     bulbs.extend(new_input().split())
#     match = {'0': '1', '1': '0'}
#
#     def command_action():
#         if command == 1:
#             bulbs[first] = str(second)
#         elif command == 2:
#             for i in range(first, second + 1):
#                 bulbs[i] = match[bulbs[i]]
#         else:
#             value = str(command - 3)
#             bulbs[first:second+1] = [value] * (second - first + 1)
#
#     for _ in range(M):
#         command, first, second = map(int, new_input().split())
#         command_action()
#
#     return ' '.join(bulbs[1:])
#
# print(main())


