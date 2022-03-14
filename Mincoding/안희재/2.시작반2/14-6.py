arr = [3,5,1,1,2,3,2]

num = list(map(int,input().split()))

for i in range(4):
    cnt = 0
    for j in range(7):
        if num[i] == arr[j]:
            cnt += 1
    print(f'{num[i]}={cnt}개')
