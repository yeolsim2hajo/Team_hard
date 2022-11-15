#221115
N = int(input())
numbers = list(map(int, input().split()))
result = sorted(numbers)
for i in range(1, N):
    for j in range(N-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(*numbers)
