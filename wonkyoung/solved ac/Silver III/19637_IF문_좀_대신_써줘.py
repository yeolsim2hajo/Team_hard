#221124
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# match = {}

# for i in range(N):
#     name, power = new_input().split()
#     power = int(power)
#     match.setdefault(power, name)

# keys = sorted(match.keys())
# key_cnt = len(keys)

# def binary_search(target):
#     first, last = 0, key_cnt - 1
#     prev_key = -1
#     while first <= last:
#         mid = (first + last)//2
#         key = keys[mid]
#         if key < target:
#             first = mid + 1
#         elif key > target:
#             last = mid - 1
#             prev_key = key
#         else:
#             return match[key]
#     if prev_key != -1:
#         return match[prev_key]
#     return match[key]

# for i in range(M):
#     target = int(new_input())
#     print(binary_search(target))


# if 없앰
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# match = {}

# for i in range(N):
#     name, power = new_input().split()
#     power = int(power)
#     match.setdefault(power, name)

# keys = sorted(match.keys())
# key_cnt = len(keys)

# def binary_search(target):
#     first, last = 0, key_cnt - 1
#     prev_key = 0
#     while first <= last:
#         mid = (first + last)//2
#         key = keys[mid]
#         if key < target:
#             first = mid + 1
#         elif key > target:
#             last = mid - 1
#             prev_key = key
#         else:
#             return match[key]
#     return match[prev_key]

# for i in range(M):
#     target = int(new_input())
#     print(binary_search(target))


# sorted 제거
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# match = {}

# for i in range(N):
#     name, power = new_input().split()
#     power = int(power)
#     match.setdefault(power, name)

# keys = list(match.keys())
# key_cnt = len(keys)

# def binary_search(target):
#     first, last = 0, key_cnt - 1
#     prev_key = 0
#     while first <= last:
#         mid = (first + last)//2
#         key = keys[mid]
#         if key < target:
#             first = mid + 1
#         elif key > target:
#             last = mid - 1
#             prev_key = key
#         else:
#             return match[key]
#     return match[prev_key]

# for i in range(M):
#     target = int(new_input())
#     print(binary_search(target))


# setdefault 대신 get 사용
import sys
new_input = sys.stdin.readline
N, M = map(int, new_input().split())
match, keys = {}, []

for i in range(N):
    name, power = new_input().split()
    power = int(power)
    if not match.get(power):
        match[power] = name
        keys.append(power)

key_cnt = len(keys)

def binary_search(target):
    first, last = 0, key_cnt - 1
    prev_key = 0
    while first <= last:
        mid = (first + last)//2
        key = keys[mid]
        if key < target:
            first = mid + 1
        elif key > target:
            last = mid - 1
            prev_key = key
        else:
            return match[key]
    return match[prev_key]

for i in range(M):
    target = int(new_input())
    print(binary_search(target))
