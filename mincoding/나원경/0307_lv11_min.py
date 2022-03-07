#lv.11
#1 함수로부터 값 보내고 받기
def input_func():
    return input()

def main():
    a, b, c = map(int, input_func().split())
    calc(a,b,c)

def calc(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)

main()


#2 함수를 이용하자

def sum_func(num, ber):
    return num + ber
def comp(a,b):
    return abs(a-b)
def print_func(a,b):
    print('합:{}\n차:{}'.format(a,b))

n, m = map(int, input().split())
print_func(sum_func(n,m),comp(n,m))

#3-5 포인터 문제
#6 값 존재여부 찾아내기
arr = [3,4,1,3,2,7,3]
n = int(input())
flag = 0
for i in arr:
    if n == i:
        flag = 1
        print('발견')
        break
else:print('미발견')

#7 MAX, MIN 찾아내기
arr = list(map(int, input().split()))
print(f'MAX={max(arr)}\nMIN={min(arr)}')

#8 문장에서 특정 값 찾아내기
munjang = 'StructPointer'
arr = list(map(str, munjang))
m = input()
if m in arr:
    print('발견')
else:
    print('미발견')

#9 원하는 글자만 다른곳에 쌓아두기 - 일부 정답
arr = input().split()
big = ['']*8
small = ['']*8
for i in range(8):
    if arr[i].isupper():
        big[i] = arr[i]
    else:
        small[i] = arr[i]
print('big=',*big,sep='')
print('small=',*small,sep='')
# 아래는 오류남
# print('big=%s\nsmall=%s'%(*big,*small),sep='')

# 다른 방법
arr = input().split()
big = []
small = []
for i in range(8):
    if arr[i].isupper():
        big.append(arr[i])
    else:
        small.append(arr[i])
print('big=',*big,sep='')
print('small=',*small,sep='')


#10 숫자 하나 입력받고 전역배열에서 값 찾기
arr = [[3,2,6,2,4],[1,4,2,6,5]]
def main():
    target = int(input())
    if kfc(target):
        print('값이 존재합니다')
    else:
        print('값이 없습니다')

def kfc(arg):
    for i in range(2):
        if arg in arr[i]:
            return 1
    return 0

main()


#11 원하는 값만 따로 빼오기
arr = [[1,3,6,2],[4,2,4,5],[6,3,7,3],[1,5,4,6]]
n = int(input())
select_arr = [0]*16
idx = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] > n:
            select_arr[idx] = arr[i][j]
            idx += 1
print(*[select_arr[i] for i in range(16) if select_arr[i] != 0])
# <generator object <genexpr> at 0x0000026182AA8B10>
# print(select_arr[i] for i in range(16) if select_arr[i] != 0)

