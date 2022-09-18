arr = [["A","7","9","T","K","Q"],["M","I","N","C","O","D"]]
str1, str2 = input().split()

def isExist(str):
    result=0
    for i in range(2):
        for j in range(6):
            if arr[i][j] == str:
                result = 1
            
    return result

if isExist(str1) :
    print("{0} : 존재".format(str1))
else:
    print("{0} : 없음".format(str1))


if isExist(str2) :
    print("{0} : 존재".format(str2))
else:
    print("{0} : 없음".format(str2))