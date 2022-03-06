arr1 = [[0,0,1,0,0],[0,0,1,1,1]]
arr2 = [[3,5,4,1,1],[3,5,2,5,6]]
# arr1의 1의 좌표값..
# 얻은 좌표값을 이용해 arr2에 해당하는 숫자 추출해서 리스트로 저장
# 입력받은 숫자와 추출받은 리스트를 비교하여 결과 출력

def get_xy(arr1):
    x = []
    y = []
    for row in range(2):
        for col in range(5):
            if arr1[row][col] == 1:
                x.append(row)
                y.append(col)
    return x, y

def isExist(arr2, num):
    new_arr = []
    result = 0
    # x,y 좌표값에 해당하는 arr2의 요소 추출하여 result에 저장
    for i in range(4):
        new_arr.append(arr2[x[i]][y[i]])

    for k in new_arr:
        if k == num:
            result = 1
    return result

#masking 된 x, y의 좌표값
x, y = get_xy(arr1)
#입력받을 숫자 값
num = int(input())


if isExist(arr2, num) :
    print("{0} 존재".format(num))
else:
    print("{0} 없음".format(num))
