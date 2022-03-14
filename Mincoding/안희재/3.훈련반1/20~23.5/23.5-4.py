arr = [[3,5,4,1], [1,1,2,3], [6,7,1,2]]
change = list(map(int,input().split()))
# 1 3 7 6
def update(num):
    if num == change[0]:
        num = change[1]
    elif num == change[1]:
        num = change[2]
    elif num == change[2]:
        num = change[3]
    elif num == change[3]:
        num = change[0]
    else:
        num = num
    return num

for i in range(3):
    for j in range(4):
        arr[i][j] = update(arr[i][j])

for i in range(3):
    print(*arr[i])