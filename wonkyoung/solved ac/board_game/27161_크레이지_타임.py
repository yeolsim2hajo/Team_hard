#230130
from sys import stdin
new_input = stdin.readline
N = int(new_input())
num = flow = 1
for _ in range(1, N+1):
    picture, text = new_input().split()
    text = int(text)
    action = 'NO'
    if picture == 'HOURGLASS':
        if text != num:
            flow = -flow
    elif text == num:
        action = 'YES'
    print(num, action)
    num = (num + flow - 1)%12 + 1