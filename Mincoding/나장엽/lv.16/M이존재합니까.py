str1 = list(input())
str2 = list(input())
str3 = list(input())

arr = str1+str2+str3


result=0

for i in range(0, len(arr)):
    if arr[i] == "M":
        result=1


if result == 1:
    print("M이 존재합니다")
else:
    print("M이 존재하지 않습니다.")