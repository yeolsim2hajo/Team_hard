lst = list(map(int,input().split()))

new_lst = [0] * len(lst)

new_lst[0] = lst[0]
for i in range(1, len(lst)):
    new_lst[i] = lst[i] + new_lst[i-1]

print(' '.join(map(str, new_lst)))