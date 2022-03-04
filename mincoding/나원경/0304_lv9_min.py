# lv9.5
#3 2차배열에서 좌표 출력하기
arr = ['DAA','BCD','EFA','AAD','FGE']
matrix = [list(map(str, arr[i])) for i in range(5)]
munja = input()
for i in range(5):
    for j in range(3):
        if matrix[i][j] == munja:
            print('(%d,%d)'% (i,j))

#4 2차배열에서 범위안에 있는 값 세기
arr = [[10,3,20],[60,30,40],[20,30,40]]
a, b = map(int, input().split())
cnt = 0
for i in range(3):
    for j in range(3):
        if a <= arr[i][j] <= b:
            cnt += 1
print(cnt)

#5 각 함수에서 대소문자 찾기
def input_func():
    global arr
    lst = input().split()
    for i in range(6):
        arr[i//3][i%3] = lst[i]

def find_upper():
    cnt = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j].isupper():
                cnt += 1
    print('대문자{}개'.format(cnt))

def find_lower():
    cnt = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j].islower():
                cnt += 1
    print('소문자{}개'.format(cnt))

arr = [[0] * 3 for _ in range(2)]
input_func()
find_upper()
find_lower()

#6 N의배수인 숫자 찾기
arr = [[3,5,14],[2,3,9],[6,2,7]]
n = int(input())
cnt = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] % n == 0:
            cnt += 1
print(cnt)

#7 구조체 문제
#8 함수에 숫자 주고 출력 하기
def bbq(arg):
    print(*list(range(1,int(arg)+1)), sep='')

def kfc(arg):
    print(arg*7)

n = int(input())
m = input()
if n % 2:
    bbq(m)
else:
    kfc(m)