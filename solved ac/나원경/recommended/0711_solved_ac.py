#17451 평행 우주
# N = int(input())
# planet = list(map(int, input().split()))
# multiple = 1
# speed = planet[0]
# def is_possible():
#     global speed
#     for i in range(1,N):
#         quot, remain = divmod(speed, planet[i])
#         if quot:
#             speed -= remain
#         else:
#             return 0
#     return 1
#
# while True:
#     if is_possible():
#         print(planet[0] * multiple)
#         break
#     multiple += 1
#     speed = planet[0] * multiple


# 거꾸로
# N = int(input())
# planet = list(map(int, input().split()))
# multiple = 1
# speed = planet[-1]
# def find_speed():
#     global speed
#     for i in range(N-1,0,-1):
#         if speed <= planet[i-1]:
#             speed = planet[i-1]
#         else:
#             speed = round((speed)/planet[i-1]) * planet[i-1]
#     return speed
# print(find_speed())


#10807 개수 세기
N = int(input())
lst = input().split()
number = input()
print(lst.count(number))
