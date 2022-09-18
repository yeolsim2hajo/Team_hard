
arr = [list(map(int, input().split())) for _ in range(4)]
# image배열의 특정 좌표를 지목하면, 2x3 사이즈의 합을 return 하는 rectSum 함수를 만들어라..
# 6번 반복해야 image의 전체 요소를 순회함.
# (0,0) (0,1) (1,0) (1,1) (2,0) (2,1) 중에 하나...

# (0,0)을 지목하면 합은 (0,0~2)(1, 0~2) 
# (0,1)을 지목하면 합은 (0,1~3)(1, 1~3)
# (1,0)을 지목하면 합은 (1,0~2)(2, 0~2)
# (1,1)을 지목하면 합은 (1,1~3)(2, 1~3)

def rectSum(arr):
    y = [0,0,1,1,2,2]
    x = [0,1,0,1,0,1]
    result = []
    
    for j in range(3):
        for k in range(2):
            sum = 0
            sum = sum + arr[y[j]][x[k]] + arr[y[j]][x[k]+1] + arr[y[j]][x[k]+2] + arr[y[j]+1][x[k]] + arr[y[j]+1][x[k]+1] + arr[y[j]+1][x[k]+2]
            result.append(sum)
    
    add1, add2 = 0, 0
    max = result[0]
    for i in range(len(result)):
        if max < result[i]:
            max = result[i]
            add1 = y[i]
            add2 = x[i]
        else:
            max = max
    return [add1, add2]
x = rectSum(arr)
print("({0},{1})".format(x[0],x[1]))
