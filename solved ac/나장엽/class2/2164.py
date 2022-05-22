import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
numbers = deque()
for number in range(1, N+1):
    numbers.append(number)

while True:
    if len(numbers) == 1:
        break
    numbers.popleft()
    temp = numbers.popleft()
    numbers.append(temp)


print(*numbers)