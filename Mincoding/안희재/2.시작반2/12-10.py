arr =[[0] * 5 for _ in range(5)]
a, b = input().split()
a = int(a)

if b == 'A':
    for i in range(4,-1,-1):
        arr[a-1][i] = chr(ord(b)+4-i)
else:
    for i in range(4,-1,-1):
        arr[a-1][i] = chr(ord(b)+4-i)

for i in range(5):
    print(*arr[i],sep='')