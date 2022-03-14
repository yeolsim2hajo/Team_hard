arr = [4,2,5,1,6,7,3]
a, b = input().split()
a1 = ord(a)-65
b1 = ord(b)-65

if a1 > b1:
    a1, b1 = b1, a1

sum = 0
for i in range(a1+1, b1):
    sum += arr[i]

print(sum)