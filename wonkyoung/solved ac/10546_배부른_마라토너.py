#221207
# 시간 초과
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# candidate = [new_input().rstrip() for _ in range(N)]
# for _ in range(N-1):
#     name = new_input().rstrip()
#     candidate.remove(name)
# print(*candidate)


# set 사용
# import sys
# from collections import defaultdict
# new_input = sys.stdin.readline
# N = int(new_input())
# candidate = set()
# already = defaultdict(int)
# for _ in range(N):
#     name = new_input().rstrip()
#     if name not in candidate:
#         candidate.add(name)
#     else:
#         already[name] += 1
# keys = set(already.keys())
# for _ in range(N-1):
#     name = new_input().rstrip()
#     if name not in keys:
#         candidate.remove(name)
#     else:
#         already[name] -= 1
#         if already[name] == -1:
#             candidate.remove(name)
# print(*candidate)


# dict 사용
# import sys
# from collections import defaultdict
# new_input = sys.stdin.readline
# N = int(new_input())
# candidate = defaultdict(int)
# for _ in range(N):
#     name = new_input().rstrip()
#     candidate[name] += 1
# keys = set(candidate.keys())
# for _ in range(N-1):
#     name = new_input().rstrip()
#     candidate[name] -= 1
#     if not candidate[name]:
#         keys.remove(name)
# print(*keys)


# dict + list - 시간초과
# import sys
# from collections import defaultdict
# new_input = sys.stdin.readline
# N = int(new_input())
# candidate = defaultdict(int)
# for _ in range(N):
#     name = new_input().rstrip()
#     candidate[name] += 1
# keys = list(candidate.keys())
# for _ in range(N-1):
#     name = new_input().rstrip()
#     candidate[name] -= 1
#     if not candidate[name]:
#         keys.remove(name)
# print(*keys)

# set + 함수형
# def main():
#     import sys
#     from collections import defaultdict
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     candidate = set()
#     already = defaultdict(int)
#
#     def fill_set_dict():
#         for _ in range(N):
#             name = new_input().rstrip()
#             if name not in candidate:
#                 candidate.add(name)
#             else:
#                 already[name] += 1
#
#     def remove_key():
#         keys = set(already.keys())
#         for _ in range(N-1):
#             name = new_input().rstrip()
#             if name not in keys:
#                 candidate.remove(name)
#             else:
#                 already[name] -= 1
#                 if already[name] == -1:
#                     candidate.remove(name)
#         last = candidate.pop()
#         return last
#
#     fill_set_dict()
#     return remove_key()
# print(main())


# return 값 변수에 넣기 - 시간 더 걸림
# def main():
#     import sys
#     from collections import defaultdict
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     candidate = set()
#     already = defaultdict(int)
#
#     def fill_set_dict():
#         for _ in range(N):
#             name = new_input().rstrip()
#             if name not in candidate:
#                 candidate.add(name)
#             else:
#                 already[name] += 1
#
#     def remove_key():
#         keys = set(already.keys())
#         for _ in range(N-1):
#             name = new_input().rstrip()
#             if name not in keys:
#                 candidate.remove(name)
#             else:
#                 already[name] -= 1
#                 if already[name] == -1:
#                     candidate.remove(name)
#         last = candidate.pop()
#         return last
#
#     fill_set_dict()
#     last = remove_key()
#     return last
#
# print(main())


# default dict X
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     candidate = set()
#     already = {}
#
#     def fill_set_dict():
#         for _ in range(N):
#             name = new_input().rstrip()
#             if name not in candidate:
#                 candidate.add(name)
#             elif already.get(name):
#                 already[name] += 1
#             else:
#                 already[name] = 2
#
#     def remove_key():
#         keys = set(already.keys())
#         for _ in range(N-1):
#             name = new_input().rstrip()
#             if name not in keys:
#                 candidate.remove(name)
#             else:
#                 already[name] -= 1
#                 if not already[name]:
#                     candidate.remove(name)
#         last = candidate.pop()
#         return last
#
#     fill_set_dict()
#     return remove_key()
#
# print(main())


# setdefault - 시간 더 걸림
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     candidate = set()
#     already = {}
#
#     def fill_set_dict():
#         for _ in range(N):
#             name = new_input().rstrip()
#             if name not in candidate:
#                 candidate.add(name)
#             else:
#                 already.setdefault(name, 1)
#                 already[name] += 1
#
#     def remove_key():
#         keys = set(already.keys())
#         for _ in range(N-1):
#             name = new_input().rstrip()
#             if name not in keys:
#                 candidate.remove(name)
#             else:
#                 already[name] -= 1
#                 if not already[name]:
#                     candidate.remove(name)
#         last = candidate.pop()
#         return last
#
#     fill_set_dict()
#     return remove_key()
#
# print(main())


# pop 변수 X
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     candidate = set()
#     already = {}
#
#     def fill_set_dict():
#         for _ in range(N):
#             name = new_input().rstrip()
#             if name not in candidate:
#                 candidate.add(name)
#             elif already.get(name):
#                 already[name] += 1
#             else:
#                 already[name] = 2
#
#     def remove_key():
#         keys = set(already.keys())
#         for _ in range(N-1):
#             name = new_input().rstrip()
#             if name not in keys:
#                 candidate.remove(name)
#             else:
#                 already[name] -= 1
#                 if not already[name]:
#                     candidate.remove(name)
#         return candidate.pop()
#
#     fill_set_dict()
#     return remove_key()
#
# print(main())


# 정리
# def main():
#     import sys
#     new_input = sys.stdin.readline
#
#     N = int(new_input())
#     candidate = set()
#     already = {}
#
#     def fill_set_dict():
#         nonlocal already, candidate
#         for _ in range(N):
#             name = new_input().rstrip()
#             if name not in candidate:
#                 candidate.add(name)
#             elif already.get(name):
#                 already[name] += 1
#             else:
#                 already[name] = 2
#
#     def remove_key():
#         nonlocal candidate, already
#         keys = set(already.keys())
#         for _ in range(N-1):
#             name = new_input().rstrip()
#             if name not in keys:
#                 candidate.remove(name)
#             else:
#                 already[name] -= 1
#                 if not already[name]:
#                     candidate.remove(name)
#         return candidate.pop()
#
#     fill_set_dict()
#
#     return remove_key()
#
# print(main())
