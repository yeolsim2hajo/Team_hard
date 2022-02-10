a = input()

sum = 0
b = 1
for i in range(len(a)-1, -1, -1):
    if int(a[i]) == 1:
        sum += b * 1
    b *= 2

c = sum * 17
result = bin(c)
print(result[2:])

# 아래 추가해서 돌리면, 런타임에러(재귀 관련)나옴. 더 간단하게 풀라는 뜻인듯
# def binary(c):
#     if c <= 1:
#         return str(c)
#     else:
#         return str(binary(c//2)) + str(c%2)

# print(binary(c))
