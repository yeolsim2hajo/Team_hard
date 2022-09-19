#11723 집합
# import sys
# M = int(input())
# numbers = set()
# new_input = sys.stdin.readline
# all_numbers = set(map(str,range(1,21)))
# for _ in range(M):
#     command = new_input().rstrip()
#     if command == 'all':
#         numbers.update(all_numbers)
#     elif command == 'empty':
#         numbers.clear()
#     else:
#         command = command.split()
#         if command[0] == 'add':
#             numbers.add(command[1])
#         else:
#             answer = 1 if command[1] in numbers else 0
#             if command[0] == 'check':
#                 print(answer)
#             elif answer:
#                 numbers.remove(command[1])
#             elif command[0] == 'toggle':
#                 numbers.add(command[1])

# answer = command[1] in numbers이든 if else 있든 시간은 비슷 (if else 없는 것이 약간 더 시간 걸림)
# import sys
# M = int(input())
# numbers = set()
# new_input = sys.stdin.readline
# all_numbers = set(map(str,range(1,21)))
# for _ in range(M):
#     command = new_input().rstrip()
#     if command == 'all':
#         numbers.update(all_numbers)
#     elif command == 'empty':
#         numbers.clear()
#     else:
#         command = command.split()
#         answer = command[1] in numbers
#         if command[0] == 'check':
#             print(int(answer))
#         elif answer:
#             numbers.remove(command[1])
#         elif command[0] in {'toggle', 'add'}:
#             numbers.add(command[1])


#DAT 이용 - 시간 더 걸림
# import sys
# M = int(input())
# numbers = [0] * 21
# new_input = sys.stdin.readline
# all_numbers = [1] * 21
# empty = numbers[:]
# for _ in range(M):
#     command = new_input().rstrip()
#     if command == 'all':
#         numbers = all_numbers[:]
#     elif command == 'empty':
#         numbers = empty[:]
#     else:
#         command = command.split()
#         command[1] = int(command[1])
#         answer = 1 if numbers[command[1]] else 0
#         if command[0] == 'check':
#             print(answer)
#         elif answer:
#             numbers[command[1]] = 0
#         elif command[0] in {'toggle', 'add'}:
#             numbers[command[1]] = 1
