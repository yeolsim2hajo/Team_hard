
arr = [[3,5,1],[3,8,1],[1,1,5]]
input = [list(map(int, input().split())) for _ in range(2)]

def masking(y,x):
    result= []
    sum = 0
    for i in range(2):
        for k in range(2):
            if input[i][k] == 1:
                sum += arr[y+i][x+k]
        result.append(sum)
    return sum





max = masking(0,0)
add1 = 0
add2 = 0
for y in range(2):
    for x in range(2):
        if max < masking(y,x):
            max = masking(y,x)
            add1 = y
            add2 = x
        else:
            max = max
        

print("({0},{1})".format(add1, add2))