arr = [['A','7','9','T','K','Q'], ['M','I','N','C','O','D']]

a, b = input().split()

def isExist(x, y):
    result_x= f'{x} : 존재'
    break_x = True
    for j in range(2):
        for k in range(6):
            if arr[j][k] == x:
                result_x = f'{x} : 존재'
                break_x = False
                break
            else:
                result_x = f'{x} : 없음'
        if (break_x == False):
            break

    result_y= f'{y} : 존재'
    break_y = True
    for j in range(2):
        for k in range(6):
            if arr[j][k] == y:
                result_y = f'{y} : 존재'
                break_y = False
                break
            else:
                result_y = f'{y} : 없음'
        if (break_y == False):
            break

    return (result_x, result_y)

print(isExist(a, b)[0])
print(isExist(a, b)[1])


# arr = [['A',7,9,'T','K','Q'], ['M','I','N','C','O','D']]

# str = input().split()

# def isExist():
#     for i in range(len(str)):
#         result = f'{str[i]}: 존재'
#         for j in range(2):
#             for k in range(6):
#                 if arr[j][k] == str[i]:
#                     break
#         else:
#             result = f'{str[i]}: 없음'
#         print(result)

# isExist()

# 처음 코드 : 하.. 중첩 반복문에서, break와 for- else 이용하기가 어렵네 자꾸 어긋나 
# 왜냐하면, break는 단 한개의 중첩문만을 깨기 때문이다...............