arr1 = [list(map(int,input().split())) for _ in range(4)]
blank = input()
arr2 = [list(map(int,input().split())) for _ in range(4)]

result = '걸리지않는다'
for i in range(4):
    for j in range(4):
        if arr1[i][j] == arr2[i][j] == 1:
            result = '걸리다'
            break

print(result)