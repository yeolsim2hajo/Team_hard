# import random as r 활용법 인지 -> 인프런에서 얻어갈 것은 여러 파이썬 내장 기능 활용법!
import random as r

lst = [chr(i) for i in range(65, 91)]

result = []

for i in range(100):
    result.append(r.sample(lst, 8))

user_input = input().split(' ')
result = []

for i in result:
    if len(set(i) & set(user_input[0])) == int(user_input[1]):
        result.append(i)

print(len(result))