lst = []
for i in range(3):
    lst.append(input())

max = len(lst[0])
idx = 0
for i in range(3):
    if max < len(lst[i]):
        max = len(lst[i])
        idx = i
    else:
        max = max

print(*lst[idx], sep='')