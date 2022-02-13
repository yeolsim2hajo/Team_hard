# 17295 엔드게임 스포일러
a = input()
print('Avengers: Endgame')

# 17496 스타후르츠
'''
스타후르츠 씨앗을 심으면 자라는데 T일이 걸립니다. i일에 스타후르츠 씨앗을 심으면 i+T일에 수확할 수 있고 수확한 날에도 같은 칸에 씨앗을 또 심을 수 있습니다.

씨앗을 심을 수 있는 빈 칸이 C개 있고 한 칸에 한 개의 스타후르츠

오늘은 여름 1일이고 N일까지 여름이 지속. N일이 지나면 더 이상 수확할 수 없습니다.

스타후르츠 한 개를 판매하면 P원을 벌 수 있습니다. 진수는 올해 여름 동안 얼마나 많은 돈을 벌 수 있을까요?
'''

N, T, C, P = map(int, input().split())

print((N-1)//T*C*P)

# 18108 1998년생인 내가 태국에서는 2541년생?!
year = int(input())
print(year-2541+1998)

# 18301 - 영어

# 20254 - 영어

# 20492 세금

money = int(input())
print(int(money * 0.78), int(money*(0.2 * 0.78 + 0.8)))

# 21300 - 영어
# 22193 - 영어
# 23234 - 영어
# 24078
# 24082
# 24086
# 24183
# 24218
# 24262 알고리즘 수업 - 알고리즘의 수행 시간 1

n = int(input())
print(1, 0)

# 24309


#------------------------Bronze IV-----------

# 1008 A/B
a, b = map(int, input().split())

print(a/b)

# 1297 TV 크기
d, h, w = map(int, input().split())
ratio = (d**2/(h**2 + w**2))**(0.5)
print(int(ratio*h), int(ratio*w))

# 1330 두 수 비교하기

a, b = [int(x) for x in input().split()]

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

# 1712 손익분기점
a, b, c = [int(x) for x in input().split()]
# a+bn < cn -> n > a/(c-b)
if c <= b:
    print(-1)
else:
    print(a//(c-b)+1)

# 2420 사파리월드
n, m = [int(x) for x in input().split()]
print(abs(n-m))

# 2480 주사위 세개
a, b, c = [int(x) for x in input().split()]
if a == b == c:
    print(10000+a*1000)
elif a != b and a != c and b !=c:
    print(max(a, b, c)*100)
elif a == b or a == c:
    print(1000+100*a)
elif b == c:
    print(1000+100*b)

# 2525 오븐 시계
a, b = [int(x) for x in input().split()]
c = int(input())
hour = (b+c)//60
if hour:
    if (a+hour)//24:
        print((a+hour)%24, b+c-hour*60)
    else:
        print(a+hour, b+c-hour*60)
else:
    print(a, b+c)

#2530 인공지능 시계 - 나중에
# a, b, c = [int(x) for x in input().split()]
# d = int(input())
# minute = c+d//60
# hour = b+minute//60
# if minute:
#     if hour:
#         if hour+a//24:
#             print(hour+a%24, )


#     else:

# else:
#     print(a, b, c+d)


# 2588 곱셈
num = int(input())
ber = int(input())
ber_1 = ber % 10
ber_2 = (ber % 100 - ber_1)//10
ber_3 = ber//100

print(num*ber_1)
print(num*ber_2)
print(num*ber_3)
print(num*ber)

# 2752 세수정렬

lst = [int(x) for x in input().split()]

for i in range(2):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i] 

if lst[0] > lst[1]:
    lst[0], lst[1] = lst[1], lst[0]

for i in range(3):
    print(lst[i], end=' ')


