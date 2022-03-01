# lv.8
#1 n까지 While 돌리자
n = int(input())
num = 1
while num <= n:
    print(num, end=' ')
    num += 1

#2 럭키7을 찾아라
arr = list(map(int, input().split()))
for i in range(5):
    if arr[i] != 7:
        print(arr[i],end=' ')
    else:break

#3 두 수의 합까지 출력 하기
def input_func():
    global a,b
    a, b = map(int,input().split())

def output():
    i = 5
    while i <= a+b:
        print(i, end=' ')
        i += 1

input_func()
output()

#4 Again, 럭키7이 나올때까지
arr = list(map(int, input().split()))
for i in range(5,-1,-1):
    print(arr[i],end=' ')
    if arr[i] == 7:
        break

#5 모든것을 보여줘
arr = [3,4,1,6,7,5]
i = 0
while arr != []:
    print(arr.pop(i), end=' ')

#6 2차배열에 값 채우고 출력하기

def input_func():
    global arr
    n = int(input())
    for i in range(3):
        for j in range(4):
            arr[i][j] = n+j+4*i
    return arr

def process():
    global arr
    for i in range(3):
        for j in range(4):
            arr[i][j] += 1
    return arr

def output():
    for i in range(3):
        for j in range(4):
            print(arr[i][j],end=' ')
        print()

arr = [[0]*4 for _ in range(3)]
input_func()
process()
output()


#7 1차배열 2개에 값 채우기
arr1 = ['B','D',5,'Q','A']
arr2 = ['Q','E','R','E','F']

def input_func():
    global a
    a = input()

def output():
    if a.islower():
        print(*arr1,sep='')
    elif a.isupper():
        print(*arr2,sep='')
    elif a.isdecimal():
        for i in range(8):
            print(chr(ord('H')-i),end='')
input_func()
output()

#8 샵무샵샵
arr = ['#','_','#','_','#','#']
for element in arr:
    if element == '#':
        print('샵',end='')
    else:
        print('무',end='')

#9 각자의 역할을 부여하자
arr = [[0]*3 for _ in range(2)]

def input_func():
    lst = input().split()
    global arr
    for i in range(2):
        for j in range(3):
            arr[i][j] = int(lst[3*i+j])
    return arr

def process():
    total = 0
    for element in arr:
        total += sum(element)
    return total

def output(arg):
    print(arg)

input_func()
output(process())

#10 Counting 하기
arr = [[4,3,1,1],[3,1,2,1],[0,0,1,2]]
n = int(input())
total = 0
for i in range(3):
    total += arr[i].count(n)
print(f'{total}개 존재합니다')

#11 다중 조건 처리하기
def starBox():
    for i in range(1,21,2):
        print(i, end=' ')

def macDoll():
    for i in range(8):
        print(chr(ord('H')-i),end=' ')

def copyBean():
    for i in range(-5,6):
        print(i, end=' ')

price = int(input())

if 2500 <= price < 3500:
    macDoll()
elif 3500 <= price <= 5000:
    starBox()
else:
    copyBean()
