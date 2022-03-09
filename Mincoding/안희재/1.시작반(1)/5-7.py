arr = [0] * 6

arr[0:3] = list(map(int,input().split()))
b = int(input())
arr[3:6] = [b +i for i in range(3)]

print(*arr)