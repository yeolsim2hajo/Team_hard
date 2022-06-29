import math 
A, B, V = map(int, input().split())

# 시간초과
# day = 0
# climing = 0
# while True:
#     day += 1
#     climing += A
#     if climing == V:
#         print(day)
#         break
#     climing -= B

day = (V - B) / (A - B)
print(math.ceil(day)) # 올림 처리 5.1일은 6일 걸린것.\
