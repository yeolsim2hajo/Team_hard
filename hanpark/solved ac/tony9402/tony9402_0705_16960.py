# 백준 16960 스위치와 램프

n, m = map(int, input().split())
check = [0]*m
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        continue
    lst1 = lst[1:]
    arr.append(lst1)
    for i in range(len(lst1)):
        check[lst1[i]-1] += 1
ans = 0
for i in range(len(arr)):
    rst = 0
    for j in range(len(arr[i])):
        if check[arr[i][j]-1] > 1:
            rst += 1
    if rst == len(arr[i]):
        ans = 1
        break
print(ans)

# 틀린 케이스가 있다고 나오는데, 뭐가 문제일까?