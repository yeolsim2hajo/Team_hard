# person = list(input().split())
# dish = list(map(int, input().split()))
person = ['손오공','야모차','메지터','비콜로']
dish = [70,10,55,40]

dict = {}
result = [[name, dish_cnt] for name, dish_cnt in zip(person, dish)]

result = sorted(result, key=lambda x:x[1], reverse=True)
# [['손오공', 70], ['메지터', 55], ['비콜로', 40], ['야모차', 10]]
for i in range(len(result)):
    dict[result[i][0]] =  i + 1

print(dict)