a, b = map(int,input().split())

arr1 = [a+i for i in range(3)]
arr2 = [b-i for i in range(3)]
arr = arr1 + arr2[::-1]

print(' '.join(map(str,arr)))