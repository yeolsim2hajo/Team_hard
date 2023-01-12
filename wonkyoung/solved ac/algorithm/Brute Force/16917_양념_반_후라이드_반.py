#221009
# A, B, C, X, Y = map(int, input().split())
# limit = max(X, Y)
# total = A * X + B * Y
#
# for i in range(1, limit+1):
#     yang = X - i if i <= X else 0
#     hu = Y - i if i <= Y else 0
#     total = min(i * 2 * C + A * yang + B * hu, total)
# print(total)


# 범위 축소
A, B, C, X, Y = map(int, input().split())
if X < Y:
    start, end = X, Y
else:
    start, end = Y, X

total = A * X + B * Y

for i in range(start, end+1):
    yang = X - i if i <= X else 0
    hu = Y - i if i <= Y else 0
    total = min(i * 2 * C + A * yang + B * hu, total)
print(total)


# 범위 축소2
A, B, C, X, Y = map(int, input().split())
total = A * X + B * Y
if X < Y:
    start, end = X, Y
    for i in range(start, end + 1):
        hu = Y - i
        total = min(i * 2 * C + B * hu, total)
else:
    start, end = Y, X
    for i in range(start, end + 1):
        yang = X - i
        total = min(i * 2 * C + A * yang, total)

print(total)

# 함수로
A, B, C, X, Y = map(int, input().split())

def conf(price, cnt):
    total = A * X + B * Y
    for i in range(start, end + 1):
        yanghu = cnt - i
        total = min(i * 2 * C + price * yanghu, total)
    return total

if X < Y:
    start, end = X, Y
    print(conf(B, Y))
else:
    start, end = Y, X
    print(conf(A, X))

# min, max, total만 비교하면?