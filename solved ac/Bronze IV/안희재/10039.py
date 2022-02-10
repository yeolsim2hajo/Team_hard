a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 40:
    a = 40
if b < 40:
    b = 40
if c < 40:
    c = 40
if d < 40:
    d = 40
if e < 40:
    e = 40

print((a+b+c+d+e)//5)


# ㅎㅎ; 안되네..
# a = list(map(int,input().split()))

# sum = 0
# for ele in a:
#     if ele < 40:
#         ele = 40
#         sum += ele
#     else:
#         ele = ele
#         sum += ele
        
# print(sum//5)