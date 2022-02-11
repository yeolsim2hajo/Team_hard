a, b, c = map(int,input().split())
d = int(input())

sum = a * 3600 + b * 60 + c
plus_sum = sum + d

hour = plus_sum // 3600
minute = plus_sum % 3600 // 60
second = plus_sum % 3600 % 60

if hour >= 24:
    hour -=24

print(hour, minute, second)

# 아래 코드 이해하기
# H, M, S = map(int, input().split())
# D = int(input()) 

# S += D % 60
# D = D // 60
# if S >= 60:
#     S -= 60
#     M += 1

# M += D % 60
# D = D // 60
# if M >= 60:
#     M -= 60
#     H += 1

# H += D % 24 -> 60이 아니라 24임 (시만 유일하게 1~23니까)
# if H >= 24:
#     H -= 24

# print(H,M,S)