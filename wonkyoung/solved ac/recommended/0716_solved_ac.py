#17451 평행 우주
# N = int(input())
# planet = list(map(int, input().split()))
#
# def find_speed():
#     speed = planet[-1]
#     for i in range(N - 2, -1, -1):
#         if speed <= planet[i]:
#             speed = planet[i]
#         elif speed%planet[i]:
#             speed = (speed//planet[i] + 1) * planet[i]
#     return speed
#
# print(find_speed())


# continue 사용 - 왜 틀렸지?
# (        if speed == planet[i]:
#             continue)

# 7
# 500 700 400 300 1000 200 600

# math.ceil - 더 빠름 - 분기 안 나누는 게 더 빠름
# N = int(input())
# planet = list(map(int, input().split()))
#
# def find_speed():
#     from math import ceil
#     speed = planet[-1]
#     for i in range(N - 2, -1, -1):
#         speed = ceil(speed/planet[i]) * planet[i]
#     return speed
#
# print(find_speed())