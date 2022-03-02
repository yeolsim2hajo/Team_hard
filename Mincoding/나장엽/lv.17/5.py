arr = [[3,5,9],[4,2,1],[5,1,5]]
num = list(map(int, input().split()))

def isExist(num):
    result=0
    for row in range(3):
        for col in range(3):
            if arr[row][col] == num:
                result = 1
            
    return result

for number in num:  
    if isExist(number) :
        print("{0}:존재".format(number))
    else:
        print("{0}:미발견".format(number))

