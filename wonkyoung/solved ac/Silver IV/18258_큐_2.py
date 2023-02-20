#230220
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         elif command == 'size':
#             print(len(q))
#         elif not q:
#             if command != 'empty':
#                 print(-1)
#             else:
#                 print(1)
#         elif command == 'empty':
#             print(0)
#         elif command == 'pop':
#             print(q.popleft())
#         elif command == 'front':
#             print(q[0])
#         else:
#             print(q[-1])
# print_command()

#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     def q_method(command):
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         elif command == 'size':
#             print(len(q))
#         elif not q:
#             if command != 'empty':
#                 print(-1)
#             else:
#                 print(1)
#         elif command == 'empty':
#             print(0)
#         elif command == 'pop':
#             print(q.popleft())
#         elif command == 'front':
#             print(q[0])
#         else:
#             print(q[-1])
#     for _ in range(N):
#         command = new_input().rstrip()
#         q_method(command)
# print_command()


#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     def q_method(command):
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         elif command == 'size':
#             return len(q)
#         elif not q:
#             if command != 'empty':
#                 return -1
#             return 1
#         elif command == 'empty':
#             return 0
#         elif command == 'pop':
#               return q.popleft()
#         elif command == 'front':
#             return q[0]
#         else:
#             return q[-1]
#     for _ in range(N):
#         command = new_input().rstrip()
#         answer = q_method(command)
#         if answer is not None:
#             print(answer)
# print_command()

#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     length = 0
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#             length += 1
#         elif command == 'size':
#             print(length)
#         elif not q:
#             if command != 'empty':
#                 print(-1)
#             else:
#                 print(1)
#         elif command == 'empty':
#             print(0)
#         elif command == 'pop':
#             print(q.popleft())
#             length -= 1
#         elif command == 'front':
#             print(q[0])
#         else:
#             print(q[-1])
# print_command()

#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         elif command == 'size':
#             print(len(q))
#         elif not q:
#             if command != 'empty':
#                 print(-1)
#             else:
#                 print(1)
#         elif command == 'empty':
#             print(0)
#         elif command == 'pop':
#             print(q.popleft())
#         elif command == 'front':
#             print(q[0])
#         else:
#             print(q[-1])
# print_command()


#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     for _ in range(N):
#         command = new_input().rstrip()
#         try:
#             if command.startswith('push'):
#                 number = command.split()[1]
#                 q.append(number)
#             elif command == 'size':
#                 print(len(q))
#             elif command == 'empty':
#                 answer = 0 if q else 1
#                 print(answer)
#             elif command == 'empty':
#                 print(0)
#             elif command == 'pop':
#                 print(q.popleft())
#             elif command == 'front':
#                 print(q[0])
#             else:
#                 print(q[-1])
#         except Exception:
#             print(-1)
# print_command()

#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         else:
#             if command == 'size':
#                 answer = len(q)
#             elif not q:
#                 answer = -1 if command != 'empty' else 1
#             elif command == 'empty':
#                 answer = 0
#             elif command == 'pop':
#                 answer = q.popleft()
#             elif command == 'front':
#                 answer = q[0]
#             else:
#                 answer = q[-1]
#             print(answer)
# print_command()


#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         else:
#             length = len(q)
#             if command == 'size':
#                 print(length)
#             elif not length:
#                 if command != 'empty':
#                     print(-1)
#                 else:
#                     print(1)
#             elif command == 'empty':
#                 print(0)
#             elif command == 'pop':
#                 print(q.popleft())
#             elif command == 'front':
#                 print(q[0])
#             else:
#                 print(q[-1])
# print_command()

#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     length = 0
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#             length += 1
#         else:
#             if command == 'size':
#                 print(length)
#             elif not length:
#                 if command != 'empty':
#                     print(-1)
#                 else:
#                     print(1)
#             elif command == 'empty':
#                 print(0)
#             elif command == 'pop':
#                 print(q.popleft())
#                 length -= 1
#             elif command == 'front':
#                 print(q[0])
#             else:
#                 print(q[-1])
# print_command()


#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     match_func = {
#         'size': lambda : len(q),
#         'empty': lambda : 0 if q else 1,
#         'pop': lambda : -1 if not q else q.popleft(),
#         'front': lambda : -1 if not q else q[0],
#         'back': lambda : -1 if not q else q[-1]
#     }
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         else:
#             print(match_func[command]())
# print_command()


#
# def print_command():
#     from sys import stdin
#     from collections import deque
#     new_input = stdin.readline
#     N = int(new_input())
#     q = deque()
#     match_func = [
#         {
#             'size': 0,
#             'empty': 1,
#             'pop': -1,
#             'front': -1,
#             'back': -1
#         },
#         {
#             'size': lambda: len(q),
#             'empty': lambda: 0,
#             'pop': lambda: q.popleft(),
#             'front': lambda: q[0],
#             'back': lambda: q[-1]
#         }
#     ]
#     for _ in range(N):
#         command = new_input().rstrip()
#         if command.startswith('push'):
#             number = command.split()[1]
#             q.append(number)
#         elif q:
#             print(match_func[1][command]())
#         else:
#             print(match_func[0][command])
# print_command()