word = input()

arr = []
for ele in word:
    arr.append(ord(ele))

arr.sort(reverse=False)

for ele in arr:
    print(chr(ele),end='')