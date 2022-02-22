#level6

#1 문자 입력받고 출력하기
# def input_munja():
#     global munja1, munja2
#     munja1, munja2= input().split()
#
# def output(*args):
#     print(*args)
#
# input_munja()
# output(munja1,munja2)

#2 아스키코드 문자번호를 밝혀라
# a, b, c = input().split()
# print(ord(a))
# print(ord(b))
# print(ord(c))

#3 1부터 5까지 n번 출력하기
# n = int(input())
#
# for _ in range(n):
#     for i in range(1,6):
#         print(i,end=' ')
#     print()

#4 배열을 모두 출력하기
# arr = ['$','@','D','A','9','#']
# for i in range(len((arr))):
#     print(f'{arr[i]}:{ord(arr[i])}')

#5 배열을 n 번 출력하기
# arr = ['B','T','K','A']
# n = int(input())
# for _ in range(n):
#     print(*arr)