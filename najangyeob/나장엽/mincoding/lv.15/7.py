arr = ['A','B','C','Z','E','T','Q']

target = list(input())
result = []
for i in range(len(target)):
    flag = 0
    for k in range(len(arr)):
        if arr[k] == target[i]:
            flag = 1
    result.append(flag)


for i in range(len(result)):
    if result[i] == 1:
        print(f'{target[i]}=마을사람')
    else:
        print(f'{target[i]}=외부사람')