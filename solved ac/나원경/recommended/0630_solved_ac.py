#2121 넷이서 놀기
import sys

N = int(input())
A, B = map(int,input().split())
new_input = sys.stdin.readline
points = set([tuple(map(int, new_input().split())) for _ in range(N)])
cnt = 0
for x,y in points:
    for dx, dy in (A, B), (A, 0), (0, B):
        if (x+dx, y+dy) not in points:
            break
    else:
        cnt += 1
print(cnt)