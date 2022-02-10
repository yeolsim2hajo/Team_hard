A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

price_A = A * P
price_B = 0

if P < C:
    price_B = B
else:
    price_B = B + (P-C)*D

print(min(price_A,price_B))
