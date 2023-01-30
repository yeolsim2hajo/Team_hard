A = []
sum = 0
for i in range(0,5):
    A.append(int(input()))

for num in A:
    if(0<=num<=100):
        sum = sum+num
print(sum)