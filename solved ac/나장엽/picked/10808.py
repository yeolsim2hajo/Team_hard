# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램

S = input();

check =[0] * 200

# for alpha in S:
#     check[ord(alpha)] += 1

# for chk in range(97, 123, 1):
#     print(check[chk], end=' ')


dictonary = dict()
for alpha in range(97, 123, 1):
  dictonary[chr(alpha)] = 0

for alpha in S:
  dictonary[alpha] += 1

print(*list(dictonary.values()), sep = ' ')





