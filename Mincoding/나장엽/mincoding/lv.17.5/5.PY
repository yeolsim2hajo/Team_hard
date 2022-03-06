
vec = [3,5,4,2,6,6,5]
bit = list(map(int, input().split()))

result = [0]*7

for i in range(0, len(bit)):
    if bit[i] == 1:
        result[i] = vec[i]

for k in range(0, len(result)):
    if result[k] != 0:
        result[k] = 7


for p in result:
    print(p, end='')