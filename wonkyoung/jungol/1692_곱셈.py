#221107
# number1 = int(input())
# number2 = int(input())
# new_number2 = number2
# for _ in range(3):
#     remain = new_number2 % 10
#     print(number1 * remain)
#     new_number2 //= 10
# print(number1 * number2)


# 합
number1 = int(input())
number2 = int(input())
result = 0
for i in range(3):
    remain = number2 % 10
    answer = number1 * remain
    print(answer)
    number2 //= 10
    result += answer * (10**i)
print(result)

#
number1 = int(input())
number2 = int(input())
result = 0
for i in range(3):
    answer = number1 * (number2 % 10)
    print(answer)
    number2 //= 10
    result += answer * (10**i)
print(result)

# 함수
def find_result():
    number1 = int(input())
    number2 = int(input())
    result = 0
    for i in range(3):
        answer = number1 * (number2 % 10)
        print(answer)
        number2 //= 10
        result += answer * (10 ** i)
    return result
print(find_result())

