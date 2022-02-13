# 15700 타일 채우기 4 - 나중에
# n, m = map(int, input().split())

# # 이칙연산
# a, b, c = map(int, input().split())
# if b>c:
#     print(int(a*b/c))
# else:
#     print(int(a/b*c))

# 15873 공백 없는 A+B

# ab = input()
# b = ab[-1]
# a = ab[:len(ab)-1]
# if b == '0':
#     b = '10'
#     a = ab[:len(ab)-2]
# print(int(a)+int(b))

# 15921 수찬은 마린보이야!! - 다시
n = int(input())
if n:
    arr = map(int, input().split())
    print(1.00)
else:
    print('divide by zero')