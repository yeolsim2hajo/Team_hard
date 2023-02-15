#230215
# N = int(input())
# num_list = list(map(int, input().split()))
# acc = num_list[-1:]
# for i in range(N-2, 0, -1):
#     acc.append(acc[-1] + num_list[i])
# acc = acc[::-1]
# total = 0
# for i in range(N-1):
#     total += num_list[i] * acc[i]
# print(total)


#
# def sumproduct():
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     acc = num_list[-1:]
#     for i in range(N - 2, 0, -1):
#         acc.append(acc[-1] + num_list[i])
#     acc = acc[::-1]
#     total = 0
#     for i in range(N - 1):
#         total += num_list[i] * acc[i]
#     return total
# print(sumproduct())


#
# def sumproduct():
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     acc = num_list[-1:]
#     for i in range(N - 2, 0, -1):
#         acc.append(acc[-1] + num_list[i])
#     total = 0
#     for i in range(N-1):
#         total += num_list[i] * acc[N-2-i]
#     return total
# print(sumproduct())


#
# def sumproduct():
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     acc = num_list[-1:]
#     total = 0
#     for i in range(N - 2, 0, -1):
#         acc.append(acc[-1] + num_list[i])
#     for i in range(N-1):
#         total += num_list[i] * acc[N-2-i]
#     return total
# print(sumproduct())

#
def sumproduct(N, num_list):
    acc = num_list[-1:]
    for i in range(N - 2, 0, -1):
        acc.append(acc[-1] + num_list[i])
    total = 0
    reversed_i = N-2
    for i in range(N-1):
        total += num_list[i] * acc[reversed_i]
        reversed_i -= 1
    return total

N = int(input())
num_list = list(map(int, input().split()))
print(sumproduct(N, num_list))