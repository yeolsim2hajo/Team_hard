arr = [10,50,40,20,30,40]

num = list(map(int,input().split()))

for i in range(6):
    cnt = 0
    for j in range(6):
        if num[i] < arr[j]:
            cnt += 1
    print(f'{num[i]}={cnt}개')