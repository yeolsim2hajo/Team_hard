lst = [list(input()) for _ in range(3)]

result = ''
for i in range(len(lst)):
    result += lst[i][len(lst[i])-1]

print(result)
