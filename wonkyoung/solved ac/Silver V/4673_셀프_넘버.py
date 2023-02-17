#230217
def find_self_num(N):
    self_num = set(range(1, N))
    for i in range(1, N):
        num = total = i
        while num:
            total += num%10
            num //= 10
        self_num.discard(total)
    return self_num
print(*find_self_num(10000), sep='\n')

#
# def find_self_num(N):
#     self_num = set(range(1, N))
#     for i in range(1, N):
#         total = i
#         while i:
#             total += i%10
#             i //= 10
#         self_num.discard(total)
#     return self_num
# print(*find_self_num(10000), sep='\n')


#
self_num = set(range(1, 10000))
for i in range(1, 10000):
    total = i
    while i:
        total += i%10
        i //= 10
    self_num.discard(total)
for num in self_num:
    print(num)

#
def print_self_num():
    self_num = set(range(1, 10000))
    for i in range(1, 10000):
        total = i
        while i:
            total += i % 10
            i //= 10
        self_num.discard(total)
    for num in self_num:
        print(num)
print_self_num()