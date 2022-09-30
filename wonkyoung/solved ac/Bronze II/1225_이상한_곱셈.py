#220930
# 시간 초과
# A, B = input().split()
# result = 0
# for i in A:
#     for j in B:
#         result += int(i)*int(j)
# print(result)


# 시간 초과
# A, B = input().split()
# result = 0
# for i in A:
#     i = int(i)
#     for j in B:
#         result += i*int(j)
# print(result)

# 합의 곱
A, B = input().split()
a_sum = b_sum = 0
for i in A:
    a_sum += int(i)
for i in B:
    b_sum += int(i)
print(a_sum * b_sum)