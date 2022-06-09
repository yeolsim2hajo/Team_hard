# 정수를 저장하는 큐를 구현 -> 입력으로 주어지는 명령을 처리
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
que = deque()

for _ in range(N):
    data = input().split()
    command = data[0]

    if command == 'push':
        number = data[1]
        que.append(number)

    elif command == 'pop':
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)

    elif command == 'size':
        print(len(que))

    elif command == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
    elif command == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)