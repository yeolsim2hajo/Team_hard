arr = [[3,5,9], [4,2,1], [5,1,5]]

lst = list(map(int,input().split()))
def isExist(num):
    result = 0
    for i in range(3):
        for j in range(3):
            if num == arr[i][j]:
                result = 1
    return result

for i in lst:
    if isExist(i):
        print(f'{i}:존재')
    else:
        print(f'{i}:미발견')

# 장엽 -갓