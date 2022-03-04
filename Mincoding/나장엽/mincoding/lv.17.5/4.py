arr = [["G","K","T"],["P","A","C"]]

str1, str2 = list(input().split())

def isExist(str1, str2, arr):
    result = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j] == str1:
                result+=1
            elif arr[i][j] == str2:
                result+=1

    return result


if isExist(str1, str2, arr) == 2:
    print('대발견')
elif isExist(str1, str2, arr) == 1:
    print('중발견')
else:
    print('미발견')