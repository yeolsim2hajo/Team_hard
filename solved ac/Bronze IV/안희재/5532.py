import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(a-(max(math.ceil(b/d), math.ceil(c/e))))


# print(a-math.ceil((b+c)/(d+e))) 처음 코드
# 이렇게 푸는게 아니구나. 문제를 잘못 이해했음