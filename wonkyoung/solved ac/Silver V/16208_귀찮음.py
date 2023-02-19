#230219
# N = int(input())
# length_list = sorted(map(int, input().split()))
# total = sum(length_list)
# cost = 0
# for i in range(N-1):
#     length = length_list[i]
#     total -= length
#     cost += total * length
# print(cost)


#
# N = int(input())
# length_list = sorted(map(int, input().split()))
# total = sum(length_list[1:])
# cost = 0
# for i in range(N-1):
#     cost += total * length_list[i]
#     total -= length_list[i+1]
# print(cost)


#
# def find_cost():
#     N = int(input())
#     length_list = sorted(map(int, input().split()))
#     total = sum(length_list[1:])
#     cost = 0
#     for i in range(N-1):
#         cost += total * length_list[i]
#         total -= length_list[i+1]
#     return cost
# print(find_cost())


#
def find_cost():
    from heapq import heapify, heappop
    N = int(input())
    length_list = list(map(int, input().split()))
    total = sum(length_list)
    heapify(length_list)
    cost = 0
    while length_list:
        length = heappop(length_list)
        total -= length
        cost += total * length
    return cost
print(find_cost())