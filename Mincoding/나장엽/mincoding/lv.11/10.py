arr = [[3,2,6,2,4],[1,4,2,6,5]]

def main(arr):
    target = int(input())
    if KFC(target, arr) : 
        print('값이 존재합니다')
    else:
        print('값이 없습니다')    
def KFC(n, arr):
    flag = 0
    for i in range(len(arr)):
        for k in range(len(arr[i])):
            if arr[i][k] == n:
                flag = 1
    return flag

main(arr)