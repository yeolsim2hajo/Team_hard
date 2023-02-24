#230224
# from sys import stdin
# new_input = stdin.readline
# N = int(new_input())
# dots = {}
# colors = []
# for _ in range(N):
#     location, color = map(int, new_input().split())
#     if dots.get(color):
#         dots[color].append(location)
#     else:
#         dots[color] = [location]
#         colors.append(color)
# total = 0
#
# def dif(arr, index):
#     return arr[index] - arr[index-1]
#
# for color in colors:
#     locations = sorted(dots[color])
#     length = len(locations)
#     for i in (1, length-1):
#         total += dif(locations, i)
#     for i in range(1, length-1):
#         total += min(dif(locations, i), dif(locations, i+1))
# print(total)


#
# def sum_length():
#     from sys import stdin
#     new_input = stdin.readline
#     N = int(new_input())
#     dots = {}
#     colors = []
#     for _ in range(N):
#         location, color = map(int, new_input().split())
#         if dots.get(color):
#             dots[color].append(location)
#         else:
#             dots[color] = [location]
#             colors.append(color)
#
#     def calc_sum():
#         def dif(arr, index):
#             return arr[index] - arr[index - 1]
#         total = 0
#         for color in colors:
#             locations = sorted(dots[color])
#             length = len(locations)
#             for i in (1, length-1):
#                 total += dif(locations, i)
#             for i in range(1, length-1):
#                 total += min(dif(locations, i), dif(locations, i+1))
#         return total
#     return calc_sum()
# print(sum_length())


#
# def sum_length():
#     from sys import stdin
#     new_input = stdin.readline
#     N = int(new_input())
#     dots = {}
#     colors = []
#     for _ in range(N):
#         location, color = map(int, new_input().split())
#         if dots.get(color):
#             dots[color].append(location)
#         else:
#             dots[color] = [location]
#             colors.append(color)
#
#     def calc_sum():
#         def dif(arr, index):
#             return arr[index] - arr[index - 1]
#         total = 0
#         for color in colors:
#             locations = sorted(dots[color])
#             length = len(locations)
#             before = dif(locations, 1)
#             total += before + dif(locations, length-1)
#             for i in range(2, length):
#                 now = dif(locations, i)
#                 total += min(before, now)
#                 before = now
#         return total
#     return calc_sum()
# print(sum_length())

#
def sum_length():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    dots = {}
    colors = []
    for _ in range(N):
        location, color = map(int, new_input().split())
        if dots.get(color):
            dots[color].append(location)
        else:
            dots[color] = [location]
            colors.append(color)

    def calc_sum():
        total = 0
        for color in colors:
            locations = sorted(dots[color])
            length = len(locations)
            before = locations[1] - locations[0]
            total += before + locations[-1] - locations[-2]
            for i in range(2, length):
                now = locations[i] - locations[i-1]
                total += min(before, now)
                before = now
        return total
    return calc_sum()
print(sum_length())