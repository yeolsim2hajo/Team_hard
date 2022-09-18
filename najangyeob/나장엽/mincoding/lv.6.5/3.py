arr1 = [0]*5
arr2 = [0]*5

n = list(map(int, input().split()))

for i in range(len(n)):
    arr1[i] = str(n[i])
    arr2[i] = str(n[i])
    
print(' '.join(arr1))
print(' '.join(arr2))