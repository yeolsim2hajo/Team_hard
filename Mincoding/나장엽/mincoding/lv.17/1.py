arr = ["M","T","K","C"]

find = input()

def isExist(arr, find):
    #! result는 초기화 되어야 한다...!
    result=0
    for str in arr:
        if str == find:
            result = 1
    return result

if isExist(arr, find):
    print("발견")
else:
    print("미발견")