num = 13
arr = []

while num != 0:
    arr.append(num%2)
    num = int(num/2)

print("".join(map(str, list(reversed(arr)))))