# #6 대소문자 판단하기
# munja = input()
# if ord('A')<= ord(munja) <= ord('Z'):
#     print('대문자입니다')
# else:print('소문자입니다')
#
# #7 2중 for문으로 # 출력 하기
# n = int(input())
# for _ in range(n):
#     for _ in range(n):
#         print('#',end='')
#     print()
#
# #8 '0'~'9'문자를 숫자로 바꾸기
# char = input()
# if ord('0')<= ord(char) <= ord('9'):
#     print(int(char)+5)
#
# #9 입력받은 문자까지 출력하기
# alp = input()
# n = ord(alp)-ord('A')
# for i in range(n+1):
#     print(chr(ord('A')+i),end='')
#
# #10 소문자를 대문자로 바꾸어주기
# alp = input()
# n = ord(alp) - ord('a') + ord('A')
# print(chr(n))
#
# #11 두개의 문자를 4번 출력하기
# a,b = input().split()
# n = ord(b)-ord(a)
# for _ in range(4):
#     for i in range(n+1):
#         print(chr(ord(a)+i),end=' ')
#     print()

#12 ABC초콜릿 모으기
flag = 0
a = b = c = 0

def input_chr():
    global a, b, c
    a, b, c = input().split()

def process():
    global flag
    if a == 'A' and b == 'B' and c == 'C':
        flag = 1

def output():
    if flag == 1:
        print('ABC를찾았다')
    else:print('못찾았다')

input_chr()
process()
output()

#13 숫자 두개를 n번 출력 하기
a,b,c = map(int, input().split())
for _ in range(c):
    print(*list(range(a,b+1)))