# #lv10
# #1 돌아오는 One Two
# def one():
#     return input()
# def two():
#     return input()
# print(one()+two())
#
# #2 대각선 긋기
# n = int(input())
# arr = [[0]*4 for _ in range(4)]
# if n%2:
#     for i in range(4):
#         arr[i][3-i] = i+1
# else:
#     for i in range(4):
#         arr[i][i] = i+1
#
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j],end=' ')
#     print()
#
# #3 KFC 주문하기
# def main():
#     kfc()
#
# def kfc():
#     val1 = chicken()
#     val2 = coke()
#     print(val1,val2,sep='')
#
# def chicken():
#     return int(input())+10
#
# def coke():
#     return input()
#
# main()
#
#
# #4 사전순으로 큰 문자 찾기
# def main():
#     val = getChar()
#     print(val)
#
# def getChar():
#     mun, ja = input().split()
#     if mun > ja:
#         return mun
#     else:
#         return ja
# main()

#5 번호 순서대로
n = int(input())
arr = [[0]*3 for _ in range(3)]
cnt = 0
if n % 5 == 1:
    for j in range(2,-1,-1):
        for i in range(2,-1,-1):
            cnt += 1
            arr[i][j] = cnt
elif n % 5 == 2:
    for i in range(2,-1,-1):
        for j in range(3):
            cnt += 1
            arr[i][j] = cnt
else:
    for j in range(3):
        for i in range(3):
            cnt += 1
            arr[i][j] = 9 + cnt

for i in range(3):
    for j in range(3):
        print(arr[i][j],end=' ')
    print()