#2751 수 정렬하기 2
# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# numbers.sort()
# print(*numbers, sep='\n')

# from sys import stdin
# new_input = stdin.readline
# N = int(new_input())
# numbers = [int(new_input()) for _ in range(N)]
# numbers.sort()
# print(*numbers, sep='\n')

#10951 A+B-4
# https://wikidocs.net/26
from sys import stdin
while True:
    numbers = stdin.readline().split()
    if not numbers: break
    A, B = map(int,numbers)
    print(A+B)

#10951 A+B-4
# https://wikidocs.net/26
# 런타임 에러
# while True:
#     numbers = input().split()
#     if not numbers: break
#     A, B = map(int,numbers)
#     print(A+B)
