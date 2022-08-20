import sys

input = sys.stdin.readline

while n := int(input()):
    arr = list(int(input()) for _ in range(n))  # 수익 리스트
    for i in range(1, n):
        arr[i] = max(arr[i], arr[i] + arr[i - 1])
    print(max(arr))