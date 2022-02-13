# 14264 정육각형과 삼각형 - 수학 문제 - 나중

# 14470 전자레인지
arr = [0]*5
for i in range(5):
    arr[i] = int(input())

a, b, c, d, e = arr
if a > 0:
    print((b-a) * e)
else:
    print((-a) * c + d + b * e)

# 14623 감정이입 - 나중
b1 = input()
b2 = input()
b1_dec = ''
b2_dec = ''
for i in b1:
    int(i)


# 14681 사분면 고르기
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# 14924 폰 노이만과 파리 - 나중

# 14935 FA - 나중


def f(number):
    return len(number) * int(str(number)[0])

x = int(input())

while x == f(x):
    f(x)


print('FA')
print('NFA')

# 15680 연세대학교
n = input()
if n == '0':
    print('YONSEI')
else:
    print('Leading the Way to the Future')

