a, b, c = input().split()
c = int(c)

a1 = ord(a)
b1 = ord(b)

result = ''
for i in range(a1,b1+1):
    result += chr(i)

for i in range(c):
    print(result)
