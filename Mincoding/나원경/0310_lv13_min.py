# lv13
#1 두 사람
def get_name():
    return input().split()
def main():
    print(min(get_name()))

main()

#2 나이로 사용될 숫자 한 개를 입력 받아주세요.

def main():
    age = int(input())
    a, b, c = moom(age)
    print(a, b, c)

def moom(arg):
    return arg-4, arg+3, arg*2

main()

#3 배열 전달하기

def main():
    munja = input()
    print('%d글자' %(string_len(munja)))

def string_len(arg):
    return len(arg)

main()

4 포인터 문제
5
def main():
    numbers = kfc()
    print(f'대문자{numbers[0]}개\n소문자{numbers[1]}개')

def kfc():
    sentence = input()
    cnt_low = cnt_up = 0
    for x in sentence:
        if x.islower():
            cnt_low += 1
        elif x.isupper():
            cnt_up += 1
    return cnt_up, cnt_low

main()


#6 좋아하는 숫자 찾기
arr = [[4,5,6,1,3,1],[2,1,3,6,3,6]]
def input_func():
    return list(map(int,input().split()))

def process(lst):
    numbers = [0] * len(lst)
    for i in range(len(lst)):
        for j in range(2):
            numbers[i] += arr[j].count(lst[i])
    return list(zip(lst, numbers))

def output(lst):
    for i in lst:
        print(f'{i[0]}={i[1]}개')
def main():
    num_zip = process(input_func())
    output(num_zip)

main()


#7 좌표값 찾아주는 함수 만들기
arr = [['A','D','F'],['Q','W','E'],['Z','X','C']]
def main():
    munja = input()
    y,x = find(munja)
    print(f'{y},{x}')

def find(arg):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == arg:
                return i,j
main()