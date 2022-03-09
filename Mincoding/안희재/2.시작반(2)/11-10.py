arr = [[3,2,6,2,4], [1,4,2,6,5]]

num = int(input())

def KFC(x):
    result = 0
    for i in range(2):
        for j in range(5):
            if arr[i][j] == x:
                result = 1
                return result
    return result

def MAIN():
    if KFC(num) == 1:
        print('값이 존재합니다')
    else:
        print('값이 없습니다')

MAIN()