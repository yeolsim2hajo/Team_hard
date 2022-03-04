lst = [0]*6

num = list(map(int, input().split()))

for i in range(len(num)):
    lst[i] = num[i]


for j in range(2, len(lst)):
    lst[j] = lst[j-2]*lst[j-1]

print(lst[-1])