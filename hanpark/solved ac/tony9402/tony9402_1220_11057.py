# 백준 11057 오르막 수

n = int(input())
lst = [1]*10
for i in range(n-1):
    for j in range(1, 10):
        lst[j] += lst[j-1]
print(sum(lst)%10007)