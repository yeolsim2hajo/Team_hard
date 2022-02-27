# 7
# 1 짝수 홀수 구분하기
arr1 = [3, 5, 2, 4, 1]
arr2 = [[9, 8], [7, 1], [3, 4]]
num = int(input())
if num % 2:
    print(*arr1, sep='')
else:
    for i in range(3):
        print(*arr2[i], sep='')

# 2 고백할까 말까
n, m = map(int, input().split())
if n < m:
    if (m - n) % 2:
        print('고백한다')
    else:
        print('짝사랑만')
elif (n - m) % 2:
    print('고백한다')
else:
    print('짝사랑만')

# 3 배열 그대로 화면에 출력
arr = [[3, 1, 1], [2, 3, 2]]
for i in range(2):
    for j in range(3):
        print(arr[i][j], end='')

# 4 유아들은 몇명일까?
arr = [int(x) for x in input().split()]
cnt = 0
for i in range(5):
    if 3 <= arr[i] <= 7:
        cnt += 1
print(cnt)

# 5 단순 채점 프로그램
score = int(input())
if score >= 80:
    print('수')
elif score >= 70:
    print('우')
elif score >= 60:
    print('미')
else:
    print('재시도')

# 6 숫자 20 맞추기
num = list(map(int, input().split()))
for i in range(4):
    if num[i] < 20:
        print('더 큰수를 입력하세요')
    elif num[i] > 20:
        print('더 작은수를 입력하세요')
    else:
        print('정답입니다')

# 7 숫자 3개중에 MAX와 MIN값 찾기
arr = list(map(int, input().split()))
max_val = min_val = arr[0]
for i in range(2):
    if arr[i] > arr[i + 1]:
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i + 1] < min_val:
            min_val = arr[i + 1]
    elif arr[i + 1] > max_val:
        max_val = arr[i + 1]
    elif arr[i] < min_val:
        min_val = arr[i]
print(f'MAX={max_val}\nMIN={min_val}')

#8 홀수 짝수는 몇개?
arr = [[3,4,1],[2,1,4],[3,3,0]]
odd = even = 0
for i in range(3):
    for j in range(3):
        if arr[i][j]%2:
            odd += 1
        else:
            even += 1
print('짝수 : {}\n홀수 : {}'.format(even,odd))

#9 다중 채점 프로그램
score = list(map(int, input().split()))
for i in range(5):
    print('{}번사람은{}점'.format(i+1,score[i]),end='')
    if score[i] >= 70:
        print('PASS')
    elif score[i] >= 50:
        print('RETEST')
    else:
        print('FAIL')

#10 문자를 2차배열에 꽉 채우고 출력하기
def input_func(arg):
    arr = [[arg]*4 for _ in range(4)]
    return arr
def output(matrix):
    for i in range(4):
        print(*matrix[i], sep='')

munja = input()
output(input_func(munja))

#11 2차 배열에 순차적으로 값 채우기
def input_func():
    num = int(input())
    return num
def process(arg):
    arr = [list(range(arg + 3*i,arg + 3 + 3*i)) for i in range(3)]
    return arr
def output(arg):
    for i in range(3):
        print(*arg[i])

output((process(input_func())))

#12 복잡한 조건에 맞게 출력하기
def bbq(arg):
    if 0 < arg < 5:
        print('초기값')
    elif 6 < arg < 10:
        print('중간값')
    else:
        print('알수없는값')

num = int(input())
if num in [3,5,7]:
    for i in range(1,11):
        print(i,end='')
elif num in [0,8]:
    for i in range(10,0,-1):
        print(i,end='')
else:
    bbq(num)

#7.5
#1 배열을 안쓰고 문제 풀어보기
num = input()
for i in range(2):
    for _ in range(3):
        print(num*(5-2*i))

2 세 곳을 지목하라
arr = [0]*6
idx = list(map(int,input().split()))
for i in range(3):
    arr[idx[i]] = 1
print(*arr)

3 다중조건일때 처리하기
def input_func():
    a, b = input().split()
    return (a,b)
def output(args):
    num0 = ord(args[0])
    num1 = ord(args[1])
    if ord('A') <= num0 <= ord('Z') and ord('A') <= num1 <= ord('Z'):
        print('대문자들')
    elif ord('A') <= num0 <= ord('Z') or ord('A') <= num1 <= ord('Z'):
        print('대소문자')
    else:
        print(*[chr(ord('a')+x) for x in range(26)],sep='')
output(input_func())

#4 숫자 채우기 연습
char = [[0]*5 for _ in range(3)]
munja = input()
for i in range(15):
    char[i//5][i%5] = chr(ord(munja)+i)
dif = ord('a') - ord('A')
print(chr(dif+ord(char[2][2])))

#5 풍성한 대문자들
char = list(map(str, input().split()))
cnt = 0
for i in range(3):
    if ord(char[i]) in range(ord('A'),ord('Z')+1):
        cnt += 1
if cnt == 3:
    print('풍족하다')
elif cnt >= 1:
    print('적절하다')
else:
    print('부족하다')

#6 지정 좌표에만 세팅
arr = [[0] *4 for _ in range(2)]
y,x = map(int, input().split())
arr[y][x] = 1
for i in range(2):
    print(*arr[i])

#7 가산점 +2
n = list(map(int,input().split()))
arr = [[0]*2 for _ in range(3)]
for i in range(6):
    arr[i//2][i%2] = n[i]+2
for i in range(3):
    for j in range(2):
        print(arr[i][j],end=' ')
    print()

