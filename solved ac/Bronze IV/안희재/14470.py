a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    sum = abs(a)*c + d + b*e
else:
    sum = (b-a)*e
print(sum)
