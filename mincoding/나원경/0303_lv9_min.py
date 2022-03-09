# lv.9
#7 짝꿍바꾸기
arr = [list(map(int, input().split())) for _ in range(6)]
cnt = 0
for i in range(6):
    if arr[i][0] < arr[i][1]:
        cnt += 1
        arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
    print(*arr[i])
print(f'{cnt}명')

#8 짝꿍바꾸기
def main():
    a, b = map(int, input().split())
    return a,b
def bbq(arg1,arg2):
    print(f'합:{arg1+arg2}')
    print(f'차:{int(arg1 - arg2)}')
    print(f'곱:{arg1*arg2}')
    print(f'몫:{arg1//arg2}')

bbq(*main())

#9 Call by value2
arr = [['F','E','W'],['D','C','A']]
def main():
    a = input()
    return a

def findCh(arg):
    for i in range(2):
        if arg in arr[i]:
            print('발견')
            return
    print('미발견')
    return

findCh(main())


#10 탐색하며 호출하기
def checkChar(arg):
    if arg.isupper():
        print('대',end='')
    else:
        print('소',end='')

arr = input().split()
for element in arr:
    checkChar(element)

#11 구조체 문제

#9.5
#1 어디에 숨었을까
arra = [2,1,2,4,5]
arrb = [[2,5,3],[4,5,7],[8,7,2]]
num = int(input())
cnt = 0
for i in range(3):
    cnt += arrb[i].count(num)
print(arra.count(num)+cnt)

#2 Index 찾아내기
arr = input().split()
print('문자A는 {}개발견'.format(arr.count('A')))
for i in range(5):
    if arr[i] == 'A':
        print('{}번'.format(i))



