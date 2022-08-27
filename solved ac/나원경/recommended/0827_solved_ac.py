#1629 곱셈
# def find_remain():
#     A, B, C = map(int, input().split())
#     remain_list = [A%C]
#     remain_set = {A%C}
#     for i in range(B-1):
#         result = (remain_list[i] * A)%C
#         if result not in remain_set:
#             remain_list.append(result)
#             remain_set.add(result)
#         else:
#             dif = remain_list.index(result)
#             length = len(remain_list)-dif
#             return remain_list[B%length+dif]
#     return remain_list[B%len(remain_list)]
# print(find_remain())


#155657 N과 M (8)
N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
def dfs(arg=0, start=0, path=''):
    if arg == M:
        print(path.rstrip())
        return
    for i in range(start, N):
        dfs(arg+1, i, path+str(numbers[i])+' ')
dfs()