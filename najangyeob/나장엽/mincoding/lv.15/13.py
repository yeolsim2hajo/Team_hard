arr = [['D','A','T','A','W'],['B','B','Q','K']]

n = int(input())

arr0 = arr[0]
arr1 = arr[1]
if n % 2 == 1:
    arr0.sort()
if n % 2 == 0:
    arr1.sort()

print(*arr0, sep='')
print(*arr1, sep='')