a = int(input())
b = 0

if a % 5 != 0:
    b = a//5 + 1
else:
    b = a//5

print(b)