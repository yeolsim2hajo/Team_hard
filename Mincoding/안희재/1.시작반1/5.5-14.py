arr = []
a, b = map(int,input().split())
for i in range(a,b+1):
    arr.append(i)

print(''.join(map(str,arr)))