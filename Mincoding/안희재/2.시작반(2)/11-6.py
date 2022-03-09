arr = [3,4,1,3,2,7,3]

num = int(input())

result = '미발견'
for i in arr:
    if i == num:
        result = '발견'
        break

print(result)