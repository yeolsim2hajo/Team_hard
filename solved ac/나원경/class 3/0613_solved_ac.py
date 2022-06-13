#9019 DSLR
# T = int(input())
# def push(option, number):
#     num_list = list(map(str, number))
#     if option == 'L':
#         num = num_list.pop(0)
#         num_list.append(num)
#     else:
#         num = num_list.pop()
#         num_list.insert(0, num)
#     return ''.join(num_list)
# def double():
#     new_number = number * 2
#     if new_number > 10000:
#         new_number %= 10000
#     return new_number
# def substract():
#     new_number = number-1 if int(number) else 9999
#     return new_number
#
# for _ in range(T):
#     A, B = input().split()
#     check = [0] * 10
#     zero = 0
#     for number in A:
#         number = int(number)
#         if number == 0:
#             zero += 1
#         else:
#             check[number] += 1
#
#     for number in B:
#         number = int(number)
#         if number == 0:
#             if zero == 0:
#                 break
#            zero -= 1
#         elif check[number]:
#             check[number] -= 1
#         else:
#             break
#     else:
#         if push('L', A) == B:


#9095 1, 2, 3 더하기
T = int(input())
numbers = [1,2,3]
def dfs(arg=0, total=0):
    global cnt
    if total > n:
        return
    if total == n:
        cnt += 1
        return
    for i in range(3):
        dfs(arg+1, total+numbers[i])
for _ in range(T):
    n = int(input())
    cnt = 0
    dfs()
    print(cnt)