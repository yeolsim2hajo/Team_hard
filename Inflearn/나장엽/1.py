# #! 1
# nums = [100, 200, 300, 400, 500]

# del(nums[3])
# del(nums[3]) # del()을 쓰면 index도 줄어든다.

# print(nums)

# #! 2
# l = [200, 100, 300]
# l.insert(2, 10000) #insert(index, value)
# print(l)

# #! 3
# l = [100,200, 300]
# print(type(l))
# # 3번

# #! 4
# a = [1, 2.22, 'p',[1,2,3]]

# for i in range(4):
#     print(type(a[i]))
    
#     # 3번 str
    
# #! 5
# a = 10
# b = 2
# for i in range(1, 5, 2):
#     a += i # 10 + 1, 11 + 3, ,,,a=14
    
# print(a+b) # 14 + 2 = 16
# #! 6
# #2번

# #! 7
# # 3, 5

# #! 8
# # 84 key가 같으면 뒤에 것이 출력

#! 9
# year = '2019'
# month = '04'
# day = '26'
# hour = '11'
# minute = '34'
# second = '27'

# print(year, month, day, sep='/', end=' ')
# print(hour, minute, second, sep=':')

#! 10

# n = int(input())
# for i in range(1, n+1): 
#     print(' '*(n-i)+'*'*(2*i-1))
#! 11
# s = 0

# for i in range(1, 101, 1):
#     s += i
# print(s)

#! 12

# class Wizard:
#     def __init__(self, health, mana, armor):
#         self.health = health
#         self.mana = mana
#         self.armor = armor
        
#     def attack(self):
#         print('파이어볼')
        
# x = Wizard(health = 545, mana = 210, armor = 10)
# print(x.health, x.mana, x.armor)
# x.attack()


#! 13
# planet = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
# n = int(input())
# print(planet[n-1])

#! 14

# n = int(input())

# if n % 3 == 0:
#     print('짝')
# else:
#     print(n)

#! 15
# str = input()

# print(f'안녕하세요. 저는 {str}입니다.')
#! 16

# str = input()

# print(str[::-1]) #거꾸로 로꾸거
#! 17

# height = int(input())

# if height >= 150:
#     print("YES")
# else:
#     print("NO")

#! 18
# import math
# score = list(map(int, input().split()))

# result = sum(score)/len(score)
# print(math.trunc(result))

#! 19
# a, b = map(int, input().split())

# print(a**b)

#! 20

# a, b = map(int, input().split())

# r1 = a // b
# r2 = a % b

# print(r1, r2)

#! 21
# x = {1,2,3,4,5}
# print(type(x))
# x = {} # dict 선언
# print(type(x))
# x = set("PYTHON")
# print(type(x))
# x = set(range(5))
# print(type(x))
# x = set()
# print(type(x))

#! 22
# 6의 배수는 6으로 나누면  나머지가 0

#! 23
# print(10/2) # 5가 아닌 5.0

#! 24
# str = input()

# print(str.upper())

#! 25
# n  = int(input())

# def abc(n):
#     result = ((n**2)*3.14)
#     return result
# print(abc(n))

#! 26
# planet = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
# planet_eng = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn', 'Uranus','Neptune']

# str = input()
# idx = 0
# for i in range(len(planet)):
#     if planet[i] == str:
#         idx = i
        
# print(planet_eng[idx])

#! 27
# name = list(input().split())
# score = list(map(int, input().split()))

# d = dict()

# for i in range(2):
#     d[name[i]] = score[i]
    
# print(d)

#! 28
# arr = ['p','y','t','h','o','n']

# for i in range(5):
#     print(*arr[i:i+2], sep='')

#! 29

# str = input()

# if ord('A') <= ord(str) <= ord('Z'):
#     print("YES")
# else:
#     print("NO")

#! 30


# str = list(input())
# str2 = list(input())
# print(len(str))
# for i in range(0, 13, 1):
#         if str[i:i+5] == str2:
#             print(i)

#! 31
#????

#! 32
# arr = list(input())
# cnt = 0

# for i in range(len(arr)):
#     if arr[i] == ' ':
#         cnt += 1
        
# print(cnt + 1)

#! 33

# arr = list(map(int, input().split()))

# for i in range(len(arr)-1, -1, -1):
#     print(arr[i], end= ' ')
#! 34
# def sorting(a):
#     result = []
#     for j in range(len(a)):
#         result.append(a[j])
#     for i in range(len(result)-1, 0, -1):
#         for k in range(i):#5 0 1 2 3 4 
#             if result[k] > result[k+1]:
#                 result[k], result[k+1] = result[k+1], result[k]
                
#     return result


# arr = list(map(int, input().split()))
# temp  = sorting(arr)

# print(temp)
# print(arr)
# if temp[0] == arr[0]:
#     print("YES")
# else:
#     print("NO")

#! 35
# def one(n):
#     def two(num):
#         result = num**n
#         return result
#     return two

# a = one(2)
# b = one(3)
# c = one(4)
# print(a(10))
# print(b(10))
# print(c(10))

#! 36
# n = int(input())

# for i in range(1, 10, 1):
#     print(n*i, end= ' ')

#! 37
# arr = list(input().split())
# name = ['원영','은비','채연']
# cnt = [0,0,0]

# for i in range(len(arr)):
#     if arr[i] == name[0]:
#         cnt[0] += 1
#     elif arr[i]==name[1]:
#         cnt[1] += 1
#     else:
#         cnt[2] += 1
        
# max = cnt[0]
# idx = 0       
# for k in range(len(cnt)):
#     if max < cnt[k]:
#         max = cnt[k]
#         idx = k
#     else:
#         max = max
        
# print(f'{name[idx]}(이)가 총 {max}표로 반장이 되었습니다.')

#! 38

