arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = list(map(int,input().split()))
result = [0] * 5

for i in range(5):
    result[i] = arr1[i] * arr2[i] + arr3[i]

print(*result)
