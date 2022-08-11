import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

bunjja = a1 * b2 + a2 * b1
bunmo = b1 * b2

my = math.gcd(bunjja, bunmo)
bunjja //= my
bunmo //= my

print(bunjja, bunmo)
 