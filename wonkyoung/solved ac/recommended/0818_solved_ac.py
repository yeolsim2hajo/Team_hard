#
import sys

new_input = sys.stdin.readline
T = int(new_input())
arr = [[0],[1], [0,2,4,8,6], [0,3,9,7,1],[0,4,6],[5],[6],[0,7,9,3,1],[0,8,4,2,6],[0,9,1],[10]]
two = [2,4,8,6]
three = [3, 9, 7, 1]
four = [4, 6]
for _ in range(T):
    a, b = map(int, new_input().split())
    if a == 1:
        answer = 1
    elif a == 2:
        answer = two[(b-1)%4]
    elif a == 3:
        answer = three[(b - 1) % 4]

    elif a%10 == 0:
        answer = 10
    else:
        answer = a**b%10
    print(answer)


for _ in range()