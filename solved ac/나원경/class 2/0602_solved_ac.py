#2805 나무 자르기
N, M = map(int, input().split())
heights = list(map(int,input().split()))
start = 0
end = max(heights)
max_height = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for height in heights:
        if height > mid:
            total += height - mid
    if total == M:
        max_height = mid
        break
    elif total > M:
        start = mid + 1
    else:
        end = mid - 1
else:
    max_height = end
print(max_height)

#10828 스택
from sys import stdin
new_input = stdin.readline
N = int(new_input())
stack = []
size = 0
for _ in range(N):
    command = new_input().rstrip()
    if command == 'top':
        answer = stack[-1] if stack else -1
    elif command == 'size':
        answer = size
    elif command == 'empty':
        answer = 0 if stack else 1
    elif command == 'pop':
        size = size - 1 if size else 0
        answer = stack.pop() if stack else -1
    else:
        size += 1
        stack.append(command.split()[1])
        continue
    print(answer)

