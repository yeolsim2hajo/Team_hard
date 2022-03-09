# #1 문자 입력받고 출력하기
# munja = input()
# print(munja*3)
#
# #2 for문으로 합 구하기
# arr = list(map(int, input().split()))
# total = 0
# for i in range(4):
#     total += arr[i]
# print(total)
#
# #3 문자배열 사용하기
# arr = ['m','i','n']
# num = int(input())
# print(arr[num])
#
# #4 숫자에 따른 함수 호출하기
# def kfc():
#     print('KFC입니다')
# def mc():
#     print('MC입니다')
# num = int(input())
# if num == 1:
#     kfc()
# elif num == 2:
#     mc()
#
# #5 함수 여러번 호출하기
# def lot():
#     print(*list(range(1,6)),sep='')
# num = int(input())
# for i in range(num):
#     lot()
#
# #6 함수 정의하고 호출하기
# def kfc():
#     print('#'*10)
# def mc():
#     print('@'*10)
# def main():
#     kfc()
#     mc()
# main()
#
# #7 배열에 값 채우고 출력하기
# arr = [0]*6
# arr[0:3] = list(map(int, input().split()))
# n = int(input())
# for i in range(3):
#     arr[i+3] = n+i
# print(*arr)
#
# #8 KFC에서 입력받고 BBQ에서 출력하기
# def kfc():
#     n = int(input())
#     return n
# def bbq(m):
#     if m > 5:
#         print('만세')
#     else:print('다시')
#
# bbq(kfc())
#
# #9 함수하나 정의하고 호출하기
# arr = ['A','B','C']
# def kfc():
#     print(*arr,sep='')
# def main():
#     n = int(input())
#     for _ in range(n):
#         kfc()
# main()
#
# #10 함수에서 배열을 거꾸로 출력하기
# def input_func ():
#     global arr
#     arr = list(map(int, input().split()))
# def output():
#     for i in range(3,-1,-1):
#         print(arr[i],end='')
# input_func()
# output()
#
# #11 변수 t를 이용하여 배열에 값 채우고 출력하기
# def main():
#     n = int(input())
#     global arr
#     arr = list(range(n,n+6))
#     print_all()
#
# def print_all():
#     for i in range(6):
#         print(arr[i])
# main()
#
# #12 모두 더한 값에 따라 함수 호출하기
# def qtr():
#     print('QTR100%')
# def bbq():
#     print('BBQ100%')
# arr = list(map(int,input().split()))
# total = 0
# for i in range(3):
#     total += arr[i]
# if total >= 10:
#     qtr()
# else:bbq()
#
# #12 입력받은 값만큼 건너띄어서 출력하기
# arr = list(map(int,'34158177369'))
# n = int(input())
# for i in range(0,11,n):
#     print(arr[i],end=' ')
#
# #5.5
# #1 함수 안에서 입력받기
# def mincoding():
#     n,m = map(int,input().split())
#     print(f'({n})({m})')
# mincoding()
#
# #2 문자에 따른 함수 호출
# def kfc():
#     print('KFC')
# def bbq():
#     print('BBQ')
#
# m = input()
# if m == 'B':
#     kfc()
#     bbq()
# elif m == 'b':
#     bbq()
# elif m == '7':
#     kfc()

#3 배열을 2개 만들어서 숫자에 값 채우기
# a, b = map(int, input().split())
# arr1 = [a]*5
# arr2 = [b]*5
#
# def print_all(lst1=arr1, lst2=arr2):
#     print(*lst1,sep='')
#     print(*lst2,sep='')
#
# print_all()

#4 변수 t를 이용하여 배열에 값 채우기
# a = [0]*5
# n = int(input())
# for i in range(5):
#     a[i] = n-i
#
# def kfc():
#     print(*a,sep='')
#
# kfc()

#5 입력받은 값 배열에 채우기
# arr = [4,1,2,3,5]
# munja = input()
# if munja == 'a' or munja == 'b' or munja == 'c':
#     print(*arr[3::-1])
# else:print(*arr[4:0:-1])

#6 해당 인덱스값 출력하기
# arr = [3,5,1,2,4,6,7]
# n,m = map(int, input().split())
# for i in range(n,m+1):
#     print(arr[i],end=' ')

#7 배열에 값 채우기
# n = int(input())
# data = list(range(n, n-4,-1))
# print(*data)

#8 배열을 앞 뒤로 채우기
# a,b = map(int, input().split())
# arr = list(range(a,a+3)) + list(range(b-2,b+1))
# print(*arr)

#9 숫자 2개 입력받아 배열에 값 채우기
# a, b = map(int, input().split())
# arr = [a + b * i for i in range(5)]
# print(*arr)

#10 숫자 1개 입력받고 값을 채우기
# n = int(input())
# arr = [n*(i+1) for i in range(6)]
# print(*arr)

#12 sum값 출력하기
# arr = list(map(int,input().split()))
# total = 0
# for i in range(5):
#     total += arr[i]
# print('합은 %d입니다' %total)

#14 변수 t의 마법
# arr = [0]*6
# a, b = map(int, input().split())
# for i in range(6):
#     arr[i] = a + i
#     if a + i == b:
#         break
# print(*arr[:i+1],sep='')