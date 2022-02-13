n, m = input().split(' ')
n = int(n)
m = int(m)
split_money = 0
remain_money = 0

if 1 <= m <= n <= 10**1000:
    split_money = n // m
    remain_money = n % m

print(split_money)
print(remain_money)