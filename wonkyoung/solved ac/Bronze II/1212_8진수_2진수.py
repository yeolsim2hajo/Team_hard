#230104
# 시간 초과
target = input()
numbers = {}
def binary_number():
    for i in range(8):
        number, str_i = i, str(i)
        numbers[str_i] = ''
        for j in range(2, -1, -1):
            div = 2**j
            numbers[str_i] += str(number//div)
            number %= div
binary_number()
answer = ''
for number in target:
    answer += numbers[number]
print(int(answer))
