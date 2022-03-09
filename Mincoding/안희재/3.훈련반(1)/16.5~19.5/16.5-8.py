# 처음 코드2(성공은했지만.. - 이딴거 짤거면 나가 뒤져욧)
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

# ----------------------------------------------------------------------------
# 처음 코드1(실패)
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
# ----------------------------------------------------------------------------

# 장엽 코드
# arr = [["A","7","9","T","K","Q"],["M","I","N","C","O","D"]]
# str1, str2 = input().split()

# def isExist(str):
#     result=0
#     for i in range(2):
#         for j in range(6):
#             if arr[i][j] == str:
#                 result = 1
            
#     return result

# if isExist(str1) :
#     print("{0} : 존재".format(str1))
# else:
#     print("{0} : 없음".format(str1))


# if isExist(str2) :
#     print("{0} : 존재".format(str2))
# else:
#     print("{0} : 없음".format(str2))

# -------------------------------------------------

# 서준 코드
# def isExist(Alpa1,arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j]==Alpa1:
#                 return '존재'
#     return '없음'

# arr=[['A',7,9,'T','K','Q'],['M','I','N','C','O','D']]
# Alpa1, Alpa2 = input().split()

# print(f'{Alpa1} : {isExist(Alpa1,arr)}')
# print(f'{Alpa2} : {isExist(Alpa2,arr)}')