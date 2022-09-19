#7287 등록
# print(169)
# print('pubhan35')

#9654 나부 함대 데이터
# print('SHIP NAME'.ljust(15,' '),'CLASS'.ljust(15,' '),'DEPLOYMENT'.ljust(11,' '), 'IN SERVICE'.ljust(10, ' '),sep='')
# print('N2 Bomber'.ljust(15,' '),'Heavy Fighter'.ljust(15,' '),'Limited'.ljust(11,' '), '21'.ljust(10, ' '),sep='')
# print('J-Type 327'.ljust(15,' '),'Light Combat'.ljust(15,' '),'Unlimited'.ljust(11,' '), '1'.ljust(10, ' '),sep='')
# print('NX Cruiser'.ljust(15,' '),'Medium Fighter'.ljust(15,' '),'Limited'.ljust(11,' '), '18'.ljust(10, ' '),sep='')
# print('N1 Starfighter'.ljust(15,' '),'Medium Fighter'.ljust(15,' '),'Unlimited'.ljust(11,' '), '25'.ljust(10, ' '),sep='')
# print('Royal Cruiser'.ljust(15,' '),'Light Combat'.ljust(15,' '),'Limited'.ljust(11,' '), '4'.ljust(10, ' '),sep='')

#10699 오늘 날짜
# from datetime import datetime
# print(datetime.date(datetime.utcnow()))

#4299 AFC 윔블던
# plus, minus = map(int,input().split())
# if plus >= minus and (plus+minus)%2 == (plus-minus)%2 == 0:
#     print((plus+minus)//2, (plus-minus)//2)
# else:
#     print(-1)

#5893 17배
# number = input()
# cnt = ten = 0
# for i in number[::-1]:
#     ten = ten + 2 ** cnt if i == '1' else ten
#     cnt += 1
# ten *= 17
# answer = ''
# while ten:
#     answer = str(ten%2) + answer
#     ten //= 2
# print(answer)


#13866 팀 나누기
# people = list(map(int,input().split()))
# total = min_dif = sum(people)
# for i in range(4):
#     for j in range(i+1,4):
#         dif = abs(total - 2 * (people[i] + people[j]))
#         if dif < min_dif:
#             min_dif = dif
# print(min_dif)


#10179 쿠폰
# T = int(input())
# for _ in range(T):
#     dollar = float(input())
#     print(f'${round(dollar*0.8, 2):.2f}')

#25083 새싹
# print(
# '         ,r\'"7',
# 'r`-_   ,\'  ,/',
# ' \. ". L_r\'',
# '   `~\/',
# '      |',
# '      |',
# sep='\n'
# )

#10872 팩토리얼
# N = int(input())
# if N == 0:
#     print(1)
# else:
#     answer = N
#     while N > 2:
#         N -= 1
#         answer *= N
#     print(answer)


#15552 빠른 A+B
import sys
T = int(input())
new_input = sys.stdin.readline
for _ in range(T):
    A, B = map(int,new_input().split())
    print(A+B)






