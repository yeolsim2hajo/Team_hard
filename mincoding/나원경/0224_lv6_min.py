#6.5
#1 ASCII값 출력하기
a, b = input().split()
print('문자\'%s\'의 아스키코드값은 %d' % (a,ord(a)))
print('문자\'%s\'의 아스키코드값은 %d' % (b,ord(b)))

#2 알파벳 거꾸로 출력하기
alp = input()
num = ord(alp)-ord('a')
for i in range(num,-1,-1):
    print(chr(i+ord('a')),end='')

#3 숫자 5개 입력받고, 배열에 값 채우기
arr1 = [0]*5
arr2 = input().split()
for i in range(5):
    arr1[i] = arr2[i]
print(*arr1)
print(*arr2)

#4 문자를 구분해주기
munja = input()
if ord('a') <= ord(munja) <= ord('z'):
    print('소문자입력!!')
elif ord('A') <= ord(munja) <= ord('Z'):
    print('대문자입력!!')
else:
    print('숫자문자입력!!')

#5 합만큼 반복 하기
a,b,c = map(int, input().split())
total = a+b+c
print('%d %d %d\n' % (a,b,c) * total )

#6 count기법 체험해보기
arr = input().split()
cnt = 0
for i in range(5):
    if ord('0') <= ord(arr[i]) <= ord('9'):
        cnt += 1
if cnt:
    print('숫자%d개발견' % cnt)
else:print('숫자미발견')

#7 문자 2개 입력받고 대소문자 바꾸기
arr = input().split()
u_to_l = ord('a') - ord('A')
for i in range(2):
    if ord('A') <= ord(arr[i]) <= ord('Z'):
        print(chr(ord(arr[i]) + u_to_l),end=' ')
    else: print(chr(ord(arr[i]) - u_to_l),end=' ')

#8 배열에 값 채우기
arr = ['']*5
char = ['']*5
munja = input()
for i in range(5):
    arr[i] = chr(ord(munja)+i)
    char[i] = chr(ord(munja) - i)
print(*arr,sep='')
print(*char,sep='')

#9 n번 반대로
arr = [5,4,1,2,7,8]
n = int(input())
for _ in range(n):
    print(*arr[::-1])

#10 세 문자 중 가장 큰 문자는?
a, b, c = input().split()
if ord(a) > ord(b) and ord(a) > ord(c):
    print('옳다%s'%a)
else:print('옳지않음')

#11 너와 나의 간격
ch1, ch2 = input().split()
print(ord(ch2)-ord(ch1))