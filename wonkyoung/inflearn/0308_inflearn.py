# #1 리스트 삭제
# num = [100,200,300,400,500]
# for _ in range(2):
#     num.pop(-1)
#
# #2 리스트의 내장 함수
# l = [200,100,300]
# l.insert(2,10000)
# print(l)
#
# #3 변수의 타입
# l = [100,200,300]
# print(type(l)) # class 'list'
#
# #4 변수의 타입2
# a = 'p'
# print(type(a)) # class 'str'
#
# #5 for문 계산
# # a+b = 16
#
# #6 False
# # 1은 True
#
# #7 변수명
# # as, 1age 변수로 사용 불가
# # 예약어, 숫자로 시작하는 변수는 사용 불가
#
# #8 딕셔너리 키 이름 중복
# # 78이 출력된다
#
# #9 sep과 end를 활용한 출력방법
# year = '2019'
# month = '04'
# day = '26'
# hour = '11'
# minute = '34'
# second = '27'
# print(year, month, day, sep='/',end=' ')
# print(hour, minute, second, sep=':')
#
# #10 별 찍기
# for i in range(5):
#     print(' ' * (4-i) +'*'*(2*i+1))
#
# #11 for를 이용한 기본 활용
# s = 0
# for i in range(100):
#     s += i
# print(s)
#
# #12 게임 캐릭터 클래스 만들기
# class Wizard():
#     def __init__(self, health, mana, armor):
#         self.health = health
#         self.mana = mana
#         self.armor = armor
#
#     @staticmethod
#     def attack():
#         print('파이어볼')
#
# x = Wizard(health = 545, mana = 210, armor = 10)
# print(x.health, x.mana, x.armor)
# x.attack()
#
#
# #13 몇 번째 행성인가요?
# arr = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
# idx = int(input())
# print(arr[idx-1])
#
#
# #14 3의 배수인가요?
# n = int(input())
# print(n) if n % 3 else print('짝')
#
#
# #15 자기소개
# name = input()
# print('안녕하세요. 저는 %s입니다.'%name)
#
#
# #16 로꾸거
# word = input()
# print(word[::-1])
#
#
# #17 놀이기구 키 제한
# height = int(input())
# print('YES') if height > 150 else print('NO')
#
#
# #18 평균 점수
# import statistics
# arr = list(map(int, input().split()))
# print(statistics.mean(arr))
#
#
# #19 제곱을 구하자
# import math
# a, b = map(int, input().split())
# print(int(math.pow(a,b)))

#
# #20 몫과 나머지
# a, b = map(int, input().split())
# print(*divmod(a,b))
#
#
# #21 set은 어떻게 만드나요?
# x = {} # 딕셔너리로 만들어짐
# print(type(x))


#22 배수인지 확인하기
# i % 6 == 0


#23 OX문제
# print(10/2)의 출력 결과는 5 (X) - 나눗셈은 항상 float
#
#
# #24 대문자로 바꿔주세요!
# name = input()
# print(name.upper())
#
# #다르게 풀기
# for char in name:
#     if ord('a') <= ord(char) <= ord('z'):
#         print(chr(ord(char)+ord('A')-ord('a')),end='')
#     else:
#         print(char,end='')
#
# #25 원의 넓이를 구하세요
# def area(arg):
#     return arg*arg*3.14
# n = int(input())
# print(area(n))
#
#
# #26 행성 문제2
# kor = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
# eng = ['Mercury','Venus','Earth','Mars','Jupyter','Saturn','Uranus','Neptune']
# name = input()
# for i in range(8):
#     if kor[i] == name:
#         print(eng[i])
#         break
#
# # 다른 방법
# system = zip(kor, eng)
# for pair in system:
#     if name == pair[0]:
#         print(pair[1])
#         break
#
# #27 딕셔너리 만들기
# names = input().split()
# scores = list(map(int,input().split()))
# test = {}
# for i in range(2):
#     test[names[i]] = scores[i]
# print(test)


# #28 2-gram
# word = input()
# for i in range(0,len(word)-1):
#     print(*word[i:i+2],sep='')
#     # print(word[i]+word[i+1])
#
# #29 대문자만 지나가세요
# alp = input()
# print('NO') if alp.islower() else print('YES')
#
#
# #30 문자열 속 문자 찾기
# sentence = input()
# word = input()
# for i in range(len(sentence)-len(word)+1):
#     if sentence[i:i+len(word)] == word:
#         print(i)
#         break
#
# # 다른 방법
# word = input()
# print(sentence.find(word))
#

#31 파이썬 자료형의 복잡도
# 시간 복잡도가 1이 아닌 것
# l[a:b]


#32 문자열 만들기
sentence = input()
print(sentence.count(' ')+1)

#다른 방법
sentence = input().split()
print(len(sentence))


#33 거꾸로 출력하기
numbers = list(map(int, input().split()))
print(*numbers[::-1])

# 다른 방법
print(*reversed(numbers))

# 다른 방법
numbers.reverse()
print(*numbers)


#34 sort 구현하기
heights = list(map(int, input().split()))
print('YES') if heights == sorted(heights) else print('NO')

# 다른 방법
for i in range(len(heights)-1):
    if heights[i] > heights[i+1]:
        print('NO')
        break
else:
    print('YES')

# 다른 방법 - 나중에 다시
# if heights[0]>=heights[1]:
#     for i in range(1,len(heights)-1):
#         if heights[i] < heights[i+1]:
#             print('NO')
#             break
#     else:
#         print('YES')
#
# if heights[0]<=heights[1]:
#        if heights[i] < heights[i+1]:
#             print('NO')
#             break
#     else:
#         print('YES')
#         break


# #35 Factory 함수 사용하기 - 나중에
# def one(n):
#     def two():
#         pass
#     return two
#
# a = one(2)
# b = one(3)
# c = one(4)
# print(a(10))
# print(b(10))
# print(c(10))


#36 구구단 출력하기
n = int(input())
for i in range(1,10):
    print(n*i, end=' ')


#37 count 사용하기
candidates = input().split()
max_name = candidates[0]
max_val = candidates.count(candidates[0])
for i in range(1,len(candidates)):
    if candidates.count(candidates[i]) > max_val:
        max_name = candidates[i]
        max_val = candidates.count(candidates[i])
print(f'{max_name}(이)가 총 {max_val}표로 반장이 되었습니다.')

# set 이용
set_name = list(set(candidates))
for i in range(len(set_name)):
    if candidates.count(set_name[i]) > max_val:
        max_name = set_name[i]
        max_val = candidates.count(set_name[i])
print(f'{max_name}(이)가 총 {max_val}표로 반장이 되었습니다.')

# dat 이용
bucket = [0]*len(set_name)
for i in range(len(set_name)):
    bucket[i] = candidates.count(set_name[i])
print(f'{set_name[bucket.find(max(bucket))]}(이)가 총 {max(bucket)}표로 반장이 되었습니다.')
