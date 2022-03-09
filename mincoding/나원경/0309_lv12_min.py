#lv12
#6 문자의 위치를 구해주는 함수 만들기
arr = list(map(str,'MINQUEST'))
def main():
    munja = ['']*3
    for i in range(3):
        munja[i] = input()
        print(f'{munja[i]}={length(munja[i])}')
def length(arg):
    return arr.index(arg)

main()

#7 문장에서 세 문자 Counting
munja = input()
length = 0
for _ in munja: # 문자열 길이 구하기
    length += 1
arr = ['']*3
for i in range(3): # 문자 입력 받기
    arr[i] = input()
    cnt = 0
    for j in range(length): # 일치하는 문자 개수 구하기
        if arr[i] == munja[j]:
            cnt += 1
    print('{}={}'.format(arr[i],cnt))

#8 범위 내 문자들 따로 빼두기
arr = list(map(str,'DATAPOWER'))
a, b = map(int, input().split())
munja = ['']*9
for i in range(a, b+1):
    munja[i]=arr[i]
    print(munja[i],end='')

#9 중첩 2중For문으로 배열 채우기
arr = [[0]*3 for _ in range(3)]
n = input()
number = 1
if n.isdigit():
    for i in range(2,-1,-1):
        for j in range(2,-1,-1):
            if i <= j:
                arr[i][j] = number
                number += 1
            else:
                arr[i][j] = ' '
elif n.isupper():
    for i in range(2,-1,-1):
        for j in range(3):
            if i >= j:
                arr[i][j] = number
                number += 1
            else:
                arr[i][j] = ' '
for i in range(3):
    print(*arr[i],sep='')


#10 한줄로 문자 채우기
number, munja = input().split()
number = int(number)
arr = [[0]*5 for _ in range(5)]
for i in range(5):
    arr[number-1][4-i] = chr(ord(munja)+i)

for i in range(5):
    print(*arr[i],sep='')

# lv.12.5
#1 구조체 문제
#2 포인터 문제

#3 배열에서 입력받은 값 찾아내기
arr = [['D','A','D'],['Q','W','Q'],['A','S','D'],['A','S','D']]
def main():
    m = input()
    find(m)

def find(arg):
    for i in range(len(arr)):
        if arg in arr[i]:
            print('존재')
            break
    else:
        print('없음')

main()


#4 테두리 채우기
arr = [[0]*5 for _ in range(5)]
n = input()
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            arr[i][j] = n
        else:
            arr[i][j] = '_'
    print(*arr[i],sep='')

# 다른 방법
for i in range(5):
    if i == 0 or i == 4:
        arr[i] = [n]*5
    else:
        arr[i] = [n]+['_']*3+[n]
    print(*arr[i],sep='')


#5 마법의 현황판
num_lst = ['45454','89898','12121','45454','67676']
board = [list(map(int, num_lst[i])) for i in range(5)]
for _ in range(5):
    y,x = map(int,input().split())
    board[y][x] += 1
    if board[y][x] == 10:
        board[y][x] = 0
for i in range(5):
    print(*board[i],sep='')

# 다른 방법
for _ in range(5):
    y,x = map(int,input().split())
    if board[y][x] != 9:
        board[y][x] += 1
    else:
        board[y][x] = 0
for i in range(5):
    print(*board[i],sep='')


#6 문장의 길이 구하기2

def main():
    sentence = input()
    print(len(sentence), sentence.count(sentence[-1]),sep='\n')

main()


#7 가장 긴 문장을 찾아내기
arr = ['']*3
len_arr = [0]*3
for i in range(3):
    arr[i] = input()
    len_arr[i] = len(arr[i])
print(arr[len_arr.index(max(len_arr))])

#8 중첩 2중으로 배열 채우기
arr = [[0]*3 for _ in range(3)]
n = int(input())
for i in range(3):
    for j in range(3):
        if i + j >= 2:
            arr[i][j] = n
            n += 1
    print(*arr[i],sep='')
