#221027
# X, Y = input().split()
# def rev(num):
#     return int(num[::-1])
# print(rev(str(rev(X) + rev(Y))))


# 다른 방법
X, Y = input().split()
def find(num):
    num = int(num)
    while num % 10 == 0:
        num //= 10
    return int(str(num)[::-1])
print(find(find(X) + find(Y)))