arr = input().split()

max = 0
result = ''
for ele in arr:
    if ord(ele) > max:
        max = ord(ele)
        result = ele

print(result)