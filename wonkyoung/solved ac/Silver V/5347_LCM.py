#230208
n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    multiple = num1 * num2
    if num1 > num2:
        num1, num2 = num2, num1
    while num1:
        num1, num2 = num2%num1, num1
    print(multiple//num2)


#
# from sys import stdin
# new_input = stdin.readline
# n = int(new_input())
# for _ in range(n):
#     num1, num2 = map(int, new_input().split())
#     multiple = num1 * num2
#     if num1 > num2:
#         num1, num2 = num2, num1
#     while num1:
#         num1, num2 = num2%num1, num1
#     print(multiple//num2)


#
def find_lcm(num1, num2):
    multiple = num1 * num2
    if num1 > num2:
        num1, num2 = num2, num1
    while num1:
        num1, num2 = num2%num1, num1
    return multiple//num2

from sys import stdin
new_input = stdin.readline
n = int(new_input())
for _ in range(n):
    num1, num2 = map(int, new_input().split())
    print(find_lcm(num1, num2))