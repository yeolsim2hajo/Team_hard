#lv14.5
#1 포인터 문제
#2 민선생의 새우 양식장
N = int(input())
for i in range(5):
    if N == 1:
        shrimp = input().split()
        print(*shrimp[:i+1])
    else:
        shrimp = input().split()
        print(*shrimp[:5-i])

#3 이중 while 연습하기
N = int(input())
row = 0
while row <= 2:
    col = 0
    while col <= 4:
        print(N, end='')
        col += 1
    print()
    row += 1

#4 구조체 문제
#5 정렬하고 배열 하나로 몰아보자

# 선택 정렬
def selection_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

버블 정렬
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# # DAT 활용 - 입력값과 출력값이 list일 필요가 없음
def use_dat(lst):
    bucket = [0]*26
    for i in range(len(lst)):
        idx = ord(lst[i]) - ord('A')
        bucket[idx] += 1
    new_lst = []
    for i in range(26):
        if bucket[i]:
            new_lst += [chr(ord('A')+ i)] * bucket[i]
        if len(new_lst) == len(lst):
            break
    return new_lst

mun = list(map(str,input()))
jang = list(map(str,input()))
# mun, jang = bubble_sort(mun), bubble_sort(jang)
# mun, jang = selection_sort(mun), selection_sort(jang)
mun, jang = use_dat(mun), use_dat(jang)
print(*mun, *jang, sep='')


#6 배열에 값 채워주기
def main():
    arr = [[' ']*3 for _ in range(3)]
    output(magic(arr))

def magic(lst):
    cnt = 1
    for i in range(3):
        for j in range(3):
            if i <= j:
               lst[i][j] = cnt
               cnt += 1
    return lst

def output(arg):
    for i in range(3):
        print(*arg[i],sep='')
main()

#lv15
#1 두 문장이 모두 같을까
mun = input()
jang = input()
if len(mun) != len(jang):
    print('다름')
else:
    for i in range(len(mun)):
        if mun[i] != jang[i]:
            print('다름')
            break
    else:print('같음')


#2 숫자 쪼개기
N = int(input())
for i in range(3,-1,-1):
    print('숫자{}'.format(N // (10**i)))
    N %= (10**i)

#3 너와 나와의 거리
arr = list(map(int, input().split()))
for i in range(5):
    if not(-3 < arr[i] - arr[i+1] < 3):
        print('재배치필요')
        break
else:print('완벽한배치')

#4 거울문장이 맞나요
mun = input()
jang = input()
if len(mun) == len(jang):
    for i in range(len(mun)):
        if mun[i] != jang[len(mun)-1-i]:
            print('거울문장아님')
            break
    else:
        print('거울문장')
else:
    print('거울문장아님')

#5 문장의 길이를 정렬하기
arr = [list(map(str, input())) for _ in range(4)]
length = [len(arr[i]) for i in range(4)]
for i in range(3):
    for j in range(i+1,4):
        if length[i] > length[j]:
            length[i], length[j] = length[j], length[i]
print(*length)

#6 개구리 문장 판별하기
sentence = input()
for i in range(len(sentence)):
    if i % 2 and sentence[i].isupper():
        print('일반문장')
        break
    elif i % 2 == 0 and sentence[i].islower():
        print('일반문장')
        break
else:
    print('개구리문장')

