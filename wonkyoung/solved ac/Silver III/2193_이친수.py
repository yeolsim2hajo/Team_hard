#230106
# 메모리 초과
N = int(input())
numbers = ['10']
next = {'0':['1', '0'], '1':['0']}
for i in range(3, N+1):
    new_numbers = []
    for number in numbers:
        index = number[-1]
        for j in next[index]:
            new_numbers.append(number + j)
    numbers = new_numbers[:]
print(len(numbers))

#
# N = int(input())
# length = [1, 1]
# for i in range(3, N+1):
#     ppre, pre = length
#     length = [pre, ppre+pre]
# print(length[-1])


# 피보나치
N = int(input())
ppre = pre = 1
for i in range(3, N+1):
    ppre, pre = pre, ppre+pre
print(pre)