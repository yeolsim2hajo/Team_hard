import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    flag = 0
    for j in p:
        if j == 'R':
            arr.reverse()
        elif j == 'D':
            if arr:
                arr.popleft()
            else:
                print("error")
                flag = 1
                break
    if flag == 0:
        print("["+",".join(arr)+"]")