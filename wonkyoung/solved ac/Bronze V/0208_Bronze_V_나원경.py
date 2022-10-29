# 7287번 - 넘어감

# 8370 Plane - 영어

# 8393 합
to_n = int(input())
total = 0
for n in range(1, to_n+1):
    total += n
print(total)

# 8437 - 외국어

# 8871 - 외국어

# 9653 스타워즈 로고 - 넘어감

# 9654 나부 함대 데이터 - 틀렸지만 비슷하므로 넘어감

print('''SHIP NAME \t CLASS \t\t DELOYMENT IN SERVICE
N2 Bomber \t Heavy Fighter \t Limited   21
J-Type 327 \t Light Combat \t Unlimited 1
NX Cruiser \t Medium Fighter  Limited   18
N1 Starfighter \t Medium Fighter  Unlimited 25
Royal Cruiser \t Light Combat \t Limited   4''')

# 10170 NFC West vs North - 넘어감
# 10171 고양이 - 넘어감
# 10172 개 - 넘어감


# 10430 나머지
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

# 10699 오늘 날짜 - 나중에

# 10718 We love kriii

print('강한친구 대한육군')
print('강한친구 대한육군')

# 10757 큰 수 A+B

a, b = map(int, input().split())
print(a+b)

# 10869 사칙연산

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# 10926 ??!

site_join = input()
print(f'{site_join}??!')

# 10998 A×B

a, b = map(int, input().split())
print(a*b)

# 11283 한글 2

han_geul = input()
print(ord(han_geul) - ord('가') + 1)

# 11382 꼬마 정민

a, b, c = map(int, input().split())
print(a+b+c)

# 11654 아스키 코드

umm = input()
print(ord(umm))

# 11924 고려대는 사랑입니다

print('고려대학교')

# 13277 큰 수 곱셈

du, su = map(int, input().split())
print(du*su)

# 14645 와이버스 부릉부릉

a, b = input().split()
c, d = input().split()
e, f = input().split()
g, h = input().split()
print('비와이')

# 14652 나는 행복합니다~

n, m, k = map(int, input().split())
x, y = divmod(k,m) # 숫자가 m개씩 정렬됨
print(x, y)

# 14928 큰 수 (BIG)

favorite = int(input())
sleep_time = favorite % 20000303
print(sleep_time)

# 15727 조별과제를 하려는데 조장이 사라졌다

geori = int(input())
if geori % 5: # 나머지가 있으면 한 번 더
    print(geori//5 + 1)
else:
    print(geori//5)

# 15733 나는 누구인가

print('I\'m Sexy')

# 15740 A+B - 9

a, b = map(int, input().split())
print(a+b)

# 15894 수학은 체육과목 입니다

n = int(input())
print(4*n) # 도형을 보면 알 수 있음

# 15962 새로운 시작

print('파이팅!!')

# 15964 이상한 기호

a, b = map(int, input().split())
print((a+b)*(a-b))

# 16170 오늘의 날짜는? - 나중

# 16394 홍익대학교

years = int(input())
print(years - 1946)

# 16430 제리와 톰

a, b = map(int, input().split())
print(b-a, b) # 분모는 동일 # 1은 분모와 분자의 수가 같음

# 17256 달달함이 넘쳐흘러
a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())
b_x, b_y, b_z = c_x - a_z, c_y//a_y, c_z - a_x
print(b_x, b_y, b_z)

