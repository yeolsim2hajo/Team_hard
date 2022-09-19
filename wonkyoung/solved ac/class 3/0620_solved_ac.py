#1780 종이의 개수
import sys

N = int(input())
paper = []
numbers = [0] * 3
new_input = sys.stdin.readline
match = {'-1':0, '0':1, '1':2}
for _ in range(N):
    paper.append(new_input().split())
    for j in range(N):
        key = paper[-1][j]
        numbers[match[key]] += 1

if numbers.count(0) == 2:
    numbers = [1 if numbers[i] else 0 for i in range(3)]

else:
    var = N
    def cut():
        for i in range(var):
            for j in range(var):
                if paper[i+di][j+dj] != number:
                    return 0
        return 1
    while var > 1:
        for di in range(0, N, var):
            for dj in range(0, N, var):
                number = paper[di][dj]
                if cut():
                    numbers[match[number]] -= var**2 - 1
        var //= 3
print(*numbers, sep='\n')



#1927 최소 힙
import heapq, sys
N = int(input())
new_input = sys.stdin.readline
arr = []
for _ in range(N):
    number = int(new_input())
    if number:
        heapq.heappush(arr, number)
    else:
        answer = heapq.heappop(arr) if arr else 0
        print(answer)