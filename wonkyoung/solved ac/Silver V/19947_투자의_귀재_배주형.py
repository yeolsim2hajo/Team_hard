#230101
from math import floor
H, Y = map(int, input().split())
five = Y//5
max_balance = H
for i in range(five+1):
    balance = H
    for _ in range(i):
        balance = floor(balance * 1.35)
    remain = Y - i*5
    three = remain//3
    for j in range(three+1):
        final_balance = balance
        for _ in range(j):
            final_balance = floor(final_balance * (1.2))
        for _ in range(remain-j*3):
            final_balance = floor(final_balance * (1.05))
        max_balance = max(max_balance, final_balance)
print(max_balance)
