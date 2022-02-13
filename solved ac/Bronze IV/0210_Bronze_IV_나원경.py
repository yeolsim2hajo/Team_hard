# 2753 윤년

# year = int(input())
# t_or_f = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
# print(int(t_or_f))

# # 3004 체스판 조각
# N = int(input())
# if N % 2:
#     print((N+1)//2 * ((N+1)//2 + 1))
# else:
#     print((N // 2 + 1)**2)

# 4299 AFC 윔블던 - 다시
# 두 팀 점수의 합과 차
# 두 팀의 경기 결과를 출력 # 득점을 많이 한 쪽을 먼저 출력
# 합과 차를 갖는 경기 결과가 없다면, -1을 출력

# plus, minus = map(int, input().split())

# if :
#     print((plus+minus)//2, (plus-minus)//2)
# else:
#     print(-1)

# 5532 방학 숙제
# L = int(input())
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# math = B//D
# lang = A//C
# if B % D:
#     math = math + 1
# if A % C:
#     lang = lang + 1
# print(L-max(math, lang))


# # 5543 상근날드
# burger_1 = int(input())
# burger_2 = int(input())
# burger_3 = int(input())
# coke = int(input())
# cider = int(input())

# print(min(burger_1, burger_2, burger_3) + min(coke, cider)-50)

# 5575 타임 카드 - 나중에
# a_time = [int(x) for x in input().split()]
# b_time = [int(x) for x in input().split()]
# c_time = [int(x) for x in input().split()]
# arr = [a_time, b_time, c_time]
# for element in arr:
#     for i in range(len(a_time)//2): 
#         print(element[i+3]-element[i], end=' ')
#     print()

# # 5596 시험 점수
# min_guk = map(int, input().split())
# man_se = map(int, input().split())
# S = sum(min_guk)
# T = sum(man_se)
# print(max(S, T))

# 5893 17배 - 나중에
# N = input()
# i = len(N)-1
# new_num = 0
# bin_lst = []
# for number in N:
#     new_num += int(number) * (2**i)
#     i -= 1
# new_num = new_num*17
# while new_num != 0:
#     bin_lst.append(str(new_num % 2))
#     new_num //= 2
# for i in range(-1, -len(bin_lst),-1):
#     print(bin_lst[i], end='')

# # 9498 시험 성적
# score = int(input())

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# 10039 평균 점수
arr = [0]*5
arr[0] = int(input())
arr[1] = int(input())
arr[2] = int(input())
arr[3] = int(input())
arr[4] = int(input())

for i in range(len(arr)):
    if arr[i] < 40:
        arr[i] = 40
print(sum(arr)//len(arr))

# 10101 삼각형 외우기
a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')


# 10156 과자
# 과자 가격, 개수, 돈
k, n, m = map(int, input().split())
if k * n <= m:
    print(0)
else:
    print(k * n - m)


# 10162 전자레인지
T = int(input())
buttons = [5*60, 60, 10]
arr = [0]*3

if T % buttons[-1]:
    print(-1)
else:
    for i in range(len(buttons)):
        if T // buttons[i]:
            arr[i] = T // buttons[i]
            T = T % buttons[i]
        print(arr[i], end=' ')

# 10179 쿠폰 - 다시
T = int(input())
for _ in range(T):
    price = int(input())
    print('${:.2f}'.format(price * 0.8))


