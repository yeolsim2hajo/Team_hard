# 백준 2193 이친수

n = int(input())
lst = [0, 1, 1]
for i in range(3, n+1):
    lst.append(lst[i-1]+lst[i-2])
print(lst[-1])