#lv10
#6 짝수 홀수 함수
def main():
    a, b = map(int,input().split())
    if (a//b) % 2:
        odd(a//b)
    else:
        even(a//b)
    print_data(a+b)

def even(arg):
    print_data(arg*2)

def odd(arg):
    print_data(arg-10)

def print_data(arg):
    print(arg)

main()


#7 리턴값 비교하기
def main():
    val1 = gop()
    val2 = sum_func()
    if val1 > val2:
        print('GOP>SUM')
    elif val1 < val2:
        print('GOP<SUM')
    else:
        print('GOP==SUM')

def gop():
    a, b = map(int, input().split())
    return a*b

def sum_func():
    a,b = map(int, input().split())
    return a+b

main()


#8 핑퐁 미션
def main():
    stone = int(input())
    ret = pingpong(stone)
    print(ret)

def pingpong(tong):
    return tong+10

main()

#9 2차 배열 채우기
arr = [[0]*4 for _ in range(4)]
cnt = 0
for j in range(3,-1,-1):
    for i in range(4):
        cnt += 1
        arr[i][j] = cnt
for i in range(4):
    print(*arr[i])

#10 배열에 Line으로 배열 값 채우기
n = int(input())
arr = [[0]*4 for _ in range(3)]
for i in range(3):
    for j in range(4):
        if j != 3-n:
            arr[2-i][3-j] = j + i*4 + 1

for i in range(3):
    print(*arr[i])

#11 암호문자 출력하기
arr = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for j in range(4):
        if arr[i][j] == 0:
            arr[i][j] = '!'
        elif arr[i][j]%2:
            arr[i][j] = '@'
        else:
            arr[i][j] = '#'
        print(arr[i][j],end='')
    print()

#12 함수안에서 CountDown
def main():
    n = input_func()
    count_down(n)
def input_func():
    return int(input())
def count_down(arg):
    print(*list(range(arg,0,-1)))

main()


#10.5
#1 2차 배열 채우기2
arr = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        arr[i][j] = i*2 + j*8 + 2
    print(*arr[i])

#2 Line으로 값 채우기
arr = [[0]*5 for _ in range(5)]
n = int(input())
for i in range(5):
    if i != n:
        for j in range(5):
            arr[i][j] = i + 5*(4-j) + 1
    else:
        arr[i] = [n]*5
    print(*arr[i])

#3 구조체 문제
#4 문자 존재여부 판단하기
arr =  ['DACCD','SDFAE','EETJH']
glob_arr = [list(map(str, arr[i])) for i in range(3)]

def input_func():
    m = input()
    if check(m):
        print('있음')
    else:
        print('없음')

def check(arg):
    for i in range(3):
        if arg in glob_arr[i]:
            return 1
    return 0

def main():
    input_func()

main()


#5 입력받은 숫자를 배열의 윗줄, 아랫줄에 채우기
num = list(map(int, input().split()))
arr = [0]*3
for i in range(3):
    arr[i] = list(range(num[i],num[i]+4))
    print(*arr[i])


#6 배열 특정 범위에 값 채우기
a, b = map(int, input().split())
arr = [0]*6
for i in range(6):
    if i not in range(a,b+1):
        arr[i] = [10+i,16+i,22+i]
    else:
        arr[i] = [7]*3
    print(*arr[i])


#7 A to Z
def main():
    print(a_to_z())

def a_to_z():
    munja = input()
    if ord(munja) - ord('A') <= (ord('Z') - ord('A'))//2:
        return 'A'
    else:
        return 'Z'

main()


# 다른 방법 (0309 추가)

def a_to_z():
    import math
    munja = input()
    if math.isclose(ord(munja), ord('A'), abs_tol=13):
        return 'A'
    else:
        return 'Z'

main()

#8 Grade Calculator
def main():
    print(calculator())

def calculator():
    score = int(input())
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

main()


#9 구조체 문제
#10 Line별 Counting하기
arr = [[1,0,0,0,0],[1,0,1,0,0],[1,1,0,1,0],[1,0,1,0,0],[0,1,0,0,1],[0,0,0,1,0],[1,1,0,0,0]]

def input_func():
    return int(input())

def main():
    output(process(input_func()))

def process(arg):
    cnt = 0
    for i in range(7):
        if arr[i][arg]:
            cnt += 1
    return cnt

def output(arg):
    print(arg)

main()

#11 run 함수에서 2차배열에 값 채우기
def main():
    n = int(input())
    run(n)

def run(arg):
    arr = [0]*3
    for i in range(3):
        if arg < 10:
            arr[i] = list(range(3*i+1,3*i+4))
        else:
            arr[i] = list(range(3*i+3,3*i,-1))
        print(*arr[i],sep='')

main()


#12 Yes or No
def main():
    print(yes_or_no())

def yes_or_no():
    n = int(input())
    if n % 3 == 0:
        return 7
    elif n % 3 == 1:
        return 35
    else:
        return 50

main()


