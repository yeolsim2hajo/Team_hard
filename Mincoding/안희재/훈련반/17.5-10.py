arr = [[3,1,9], [7,2,1], [1,0,8]]

mask = []

for i in range(3):
    lst = list(map(int,input().split()))
    mask.append(lst)


def isExist():
    result = 0
    for i in range(3):
        for j in range(3):
            if mask[i][j] == 1:
                if arr[i][j] >= 3 and arr[i][j] <= 5:
                    result = 1
                    break # 아 근데 여기에서는 +=1 이런게 아니라 break굳이 안 써줘도 되네
    return result

if isExist():
    print('발견')
else:
    print('미발견')

# 와우 한번에 푼건 처음이네