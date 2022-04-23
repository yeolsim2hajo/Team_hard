# lv15
# 이중 while로 배열에 값 채우기
# arr = [['']*3 for _ in range(3)]
# alp = input()
# row = 2
# cnt = 0
# while row >= 0:
#     col = 0
#     while col + row <= 2:
#         arr[row][col] = chr(ord(alp)+cnt)
#         col += 1
#         cnt += 1
#     row -= 1
#
# for i in range(3):
#     print(*arr[i],sep='')


# lv15.5
#1 Hello World - 넘어감
#2 입력 받은 숫자보다 더 큰값 Counting
# arr = [list(map(int, x)) for x in ['51426','35007','99831']]
# N = int(input())
# cnt = 0
# for i in range(3):
#     for j in range(5):
#         if arr[i][j] > N:
#             cnt += 1
# print(f'{cnt}개')


#3 한 줄 채우기
# arr = [list(range(12-4*i, 8-4*i,-1)) for i in range(3)]
# N = int(input())
# arr[N-1] = [7]*4
# for i in range(3):
#     print(*arr[i])


#4 그가 사는 그집
# juso = [402,401,302,301,202,201,102,101]
# name = [list(map(str,x)) for x in ['KIM','TEA','SOM','OPPO','TOM','GDK','JAME','MIN']]
# hosu = int(input())
# print(*name[juso.index(hosu)],sep='')


#5 자료 출력
# a, b, c = map(int,input().split())
# for _ in range(c):
#     for x in range(a,a+b):
#         print(x, end=' ')
#     print()


#6 연속된 값 세팅하기
# arr = [0]*9
# for _ in range(3):
#     start, end = map(int, input().split())
#     for i in range(start,end+1):
#         arr[i] += 1
# print(*arr)

# 이렇게도 가능
# arr[start:end+1] = [arr[i]+ 1 for i in range(start,end+1)]


#7, 8 구조체, 포인터 문제

#9 2차 배열 정렬하기
# how = input().split()
# if len(how) == 3:
#     arr = [list(map(int, x)) for x in [how,input().split()]]
#     lst = [arr[i//3][i%3] for i in range(6)]
# else:
#     lst = list(map(int, how))
# for i in range(5):
#     for j in range(i+1,6):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(*lst[:3])
# print(*lst[3:])


#10 선택한 칸 모두 출력하기
# arr = [list(map(str,x)) for x in ['FRQWT','GASYQ','ASADB']]
# n = int(input())
# for i in range(3):
#     print(arr[i][n],end='')


#11 알파벳 퀴즈
# arr = ['A','P','P','L','E','T']
# hubo = input().split()
# total = 0
# for alp in hubo:
#     total += arr.count(alp)
# print('{}개 맞추었습니다'.format(total))


#12 번호순서대로 배열 채우기
# num = int(input())
# arr = [0]*4
# for i in range(4):
#     n = i % 2
#     m = (i+1) % 2
#     arr[i] = range(4*(i+n)+num-n,4*(i+m)+num-n,(-1)**n)
#     print(*arr[i])